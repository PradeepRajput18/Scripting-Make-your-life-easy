import os
import shutil

def organize_documents(source_directory, main_destination_directory):
    """
    Collects Excel, PowerPoint, and Word files from a source directory (and its subdirectories),
    renames them sequentially with an index and their original filename, and moves them
    into type-specific subfolders within a specified main destination directory.

    Args:
        source_directory (str): The path to the directory to search for documents.
        main_destination_directory (str): The path to the main directory where
                                          type-specific subfolders will be created.
    """

    if not os.path.exists(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return

    # Define file types and their extensions, and the names for their subfolders
    document_types = {
        "Excel": ('.xls', '.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm'),
        "PowerPoint": ('.ppt', '.pptx', '.pptm', '.potx', '.potm', '.ppsx', '.ppsm'),
        "Word": ('.doc', '.docx', '.docm', '.dotx', '.dotm')
    }

    # Create a reverse lookup for extensions to folder names for efficient checking
    extension_to_type = {}
    for doc_type, extensions in document_types.items():
        # Ensure subdirectories are created within the main destination
        type_destination_path = os.path.join(main_destination_directory, doc_type)
        os.makedirs(type_destination_path, exist_ok=True)
        for ext in extensions:
            extension_to_type[ext] = doc_type

    collected_files_by_type = {doc_type: [] for doc_type in document_types.keys()}
    total_collected_count = 0

    print(f"Scanning '{source_directory}' for documents...")

    # Walk through the source directory and its subdirectories
    for root, _, files in os.walk(source_directory):
        for file in files:
            file_name, ext = os.path.splitext(file)
            ext_lower = ext.lower()

            if ext_lower in extension_to_type:
                doc_type = extension_to_type[ext_lower]
                file_path = os.path.join(root, file)
                collected_files_by_type[doc_type].append(file_path)
                total_collected_count += 1
    
    if total_collected_count == 0:
        print(f"No Excel, PowerPoint, or Word documents found in '{source_directory}'.")
        return

    print(f"Found {total_collected_count} document(s) in total.")
    print(f"Moving and renaming documents to '{main_destination_directory}'...")

    # Process each document type
    for doc_type, files_list in collected_files_by_type.items():
        if not files_list:
            print(f"No {doc_type} documents found.")
            continue

        type_destination_path = os.path.join(main_destination_directory, doc_type)
        print(f"\nProcessing {len(files_list)} {doc_type} document(s) into '{type_destination_path}'...")

        for i, old_path in enumerate(files_list):
            # Get the original file extension (e.g., '.xlsx')
            _, ext = os.path.splitext(old_path)
            
            # Get the original filename without its path or extension (e.g., 'Quarterly_Report')
            original_filename_base = os.path.splitext(os.path.basename(old_path))[0]
            
            # Create the new filename: index_originalfilename.extension
            # The index is formatted to have at least three digits (e.g., 001, 002)
            new_filename = f"{i+1:03d}_{original_filename_base}{ext.lower()}" 
            new_path = os.path.join(type_destination_path, new_filename)

            try:
                shutil.move(old_path, new_path)
                print(f"Moved and renamed '{os.path.basename(old_path)}' to '{new_filename}'")
            except Exception as e:
                print(f"Error moving '{os.path.basename(old_path)}' to '{new_path}': {e}")

    print("\nDocument organization complete!")


if __name__ == "__main__":
    # --- Configuration ---
    # Replace with the directory where your documents are currently located
    SOURCE_FOLDER = r"C:\Users\rekka\Downloads" 
    
    # Replace with the main directory where you want to store the organized documents.
    # Subfolders (e.g., 'Excel', 'PowerPoint', 'Word') will be created inside this.
    MAIN_DESTINATION_FOLDER = r"C:\Users\rekka\OneDrive\Documents\Collected_Documents"
    
    # --- End Configuration ---

    # Ensure the source and main destination folders are not the same
    # to avoid moving files into themselves or other unexpected behavior.
    if os.path.abspath(SOURCE_FOLDER) == os.path.abspath(MAIN_DESTINATION_FOLDER):
        print("Error: Source and main destination folders must be different to prevent data loss or issues.")
        exit(1)

    # Call the function to organize the documents
    organize_documents(SOURCE_FOLDER, MAIN_DESTINATION_FOLDER)