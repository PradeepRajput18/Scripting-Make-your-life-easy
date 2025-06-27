
import os
import shutil



def organize_image(source_folder, destination_folder):

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    image_file_extentions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

    collected_images=[]

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(image_file_extentions):
                file_path = os.path.join(root,file)
                collected_images.append(file_path)
    
    if not collected_images:
        print("No images found in the source folder.")
        return
    
    print(f"Found {len(collected_images)} image(s) in '{source_folder}'.")
    print(f"Moving and renaming images to '{destination_folder}'...")


    for i,old_path in enumerate(collected_images):

        _,ext= os.path.splitext(old_path)

        original_filename_base = os.path.splitext(os.path.basename(old_path))[0]

        new_filename = f"{i+1}_{original_filename_base}{ext.lower()}"
        new_path = os.path.join(destination_folder,new_filename)

        try:
            shutil.move(old_path, new_path)
            print(f"Moved: {old_path} to {new_path}")
        except Exception as e:
            print(f"Error moving {old_path} to {new_path}: {e}")
    
    print("Image organization complete.")





    








if __name__ == "__main__":

    source_folder = r"C:\Users\rekka\Downloads"

    Destination_Folder = r"C:\Users\rekka\OneDrive\Documents\Collected_Images"
    # Ensure the source and destination folders are not the same to avoid moving files into themselves
    if os.path.abspath(source_folder) == os.path.abspath(Destination_Folder):
        print("Source and destination folders must be different.")
        exit(1)

    organize_image(source_folder,Destination_Folder)






