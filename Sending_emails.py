import smtplib
import os
from email.message import EmailMessage

import logging 





# Setting up logging 
logging.basicConfig(level=logging.INFO)


# email set up 
EMAIL_ADDRESS = 'Your email'
EMAIL_PASSWORD = "Password" #app password



def send_email(subject,recipient,body,html_content=None,attachement_path=None):
    msg = EmailMessage()
    msg['Subject']=subject
    msg['From']=EMAIL_ADDRESS
    msg['To']=recipient


    msg.set_content(body)


    if(html_content):
        msg.add_alternative(html_content, subtype='html')


    if attachement_path and os.path.isfile(attachement_path):
        try:
            with open(attachement_path, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(attachement_path)
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            logging.info(f"Attachment '{file_name}' added to the email.")
        except Exception as e:
            logging.error(f"Failed to attach file '{attachement_path}': {e}")
            return
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        logging.info(f"Email sent to {recipient} with subject '{subject}'.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        return 
    




send_email('Test Subject', 'to email', 'This is the email body',
           '<html><body><h1>HTML Content</h1></body></html>')
