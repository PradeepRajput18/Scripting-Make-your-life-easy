
import os
import shutil



def organize_pdf(source_folder, destination_folder):

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    pdf_file_extentions = ('.pdf', '.PDF')

    collected_pdfs=[]

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(pdf_file_extentions):
                file_path = os.path.join(root,file)
                collected_pdfs.append(file_path)
    
    if not collected_pdfs:
        print("No pdfs found in the source folder.")
        return
    
    print(f"Found {len(collected_pdfs)} pdfs in '{source_folder}'.")
    print(f"Moving and renaming pdfs to '{destination_folder}'...")


    for i,old_path in enumerate(collected_pdfs):

        _,ext= os.path.splitext(old_path)

        original_filename_base = os.path.splitext(os.path.basename(old_path))[0]

        new_filename = f"{i+1}_{original_filename_base}{ext.lower()}"
        new_path = os.path.join(destination_folder,new_filename)

        try:
            shutil.move(old_path, new_path)
            print(f"Moved: {old_path} to {new_path}")
        except Exception as e:
            print(f"Error moving {old_path} to {new_path}: {e}")
    
    print("PDF organization complete.")





    








if __name__ == "__main__":

    source_folder = r"C:\Users\rekka\Downloads"

    Destination_Folder = r"C:\Users\rekka\OneDrive\Documents\Collected_PDFS"
    # Ensure the source and destination folders are not the same to avoid moving files into themselves
    if os.path.abspath(source_folder) == os.path.abspath(Destination_Folder):
        print("Source and destination folders must be different.")
        exit(1)

    organize_pdf(source_folder,Destination_Folder)






