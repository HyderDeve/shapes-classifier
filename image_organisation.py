import os
from pathlib import Path

def rename_images_in_folders(base_path, student_id):
    """
    Rename all images in their respective shape folders.
    
    Args:
        base_path: Path to the shapes_dataset folder
        student_id: Your student ID (e.g., '2401bscs001')
    """
    # Define the shape folders
    shapes = ['Circle', 'Diamond', 'Pentagon', 'Square', 'Triangle']
    
    for shape in shapes:
        shape_folder = os.path.join(base_path, shape)
        
        # Check if folder exists
        if not os.path.exists(shape_folder):
            print(f"Warning: Folder '{shape}' not found at {shape_folder}")
            continue
        
        # Get all image files in the folder
        image_files = []
        for file in os.listdir(shape_folder):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(file)
        
        # Sort files to maintain consistent ordering
        image_files.sort()
        
        # Rename each image
        for index, old_filename in enumerate(image_files, start=1):
            old_path = os.path.join(shape_folder, old_filename)
            
            # Get file extension
            _, ext = os.path.splitext(old_filename)
            
            # Create new filename: shape_studentid_number.extension
            new_filename = f"{shape.lower()}_{student_id}_{index}{ext}"
            new_path = os.path.join(shape_folder, new_filename)
            
            # Rename the file
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {old_filename}: {e}")
        
        print(f"Completed renaming in '{shape}' folder\n")

if __name__ == "__main__":
    # Configuration
    # Update these values according to your setup
    
    # Path to your shapes_dataset folder
    BASE_PATH = r"C:/Users/YourUsername/OneDrive/shapes/shapes_dataset"
    
    # Your student ID
    STUDENT_ID = "2401bscs001"
    
    print("="*60)
    print("Image Renaming Script")
    print("="*60)
    print(f"Base Path: {BASE_PATH}")
    print(f"Student ID: {STUDENT_ID}")
    print("="*60)
    print()
    
    # Check if base path exists
    if not os.path.exists(BASE_PATH):
        print(f"Error: Base path '{BASE_PATH}' does not exist!")
        print("Please update the BASE_PATH variable in the script.")
    else:
        # Run the renaming function
        rename_images_in_folders(BASE_PATH, STUDENT_ID)
        print("="*60)
        print("Renaming complete!")
        print("="*60)