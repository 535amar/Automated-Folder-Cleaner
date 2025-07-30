import os
import shutil

def clean_folder(target_folder):
    """ 
    Organize files in the target folder by their file entensions.
    files will be moved into folder names after their extension types
    """
    # Loop Through eacg file in the folder
    for filename in os.listdir(target_folder):
        filepath = os.path.join(target_folder, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Extract file extension
        if '.' in filename:
            ext = filename.rsplit('.', 1)[-1].lower()
        else:
            ext = 'others' # For files with no extension

        
        # Create folder if it doesn't exist
        ext_folder = os.path.join(ext_folder, filename)
        os.makedirs(ext_folder, exist_ok = True)


        # Move file into the new folder
        shutil.move(filepath, os.path.join(ext_folder, filename))
        print(f"Moved: {filename}  {ext.upper()}/")


if __name__ == "__main__":
    folder_path = "." # Current directory
    print("Cleaning folder:", os.path.abspath(folder_path))
    clean_folder(folder_path)
    print("Cleaning complete.")