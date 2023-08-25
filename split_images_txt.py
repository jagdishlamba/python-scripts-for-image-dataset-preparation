import os
import shutil


def split_files(source_dir, destination_dir):
    # Create destination directories if they don't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Check if it's a text file
        if filename.endswith('.txt'):
            # Move the text file to the "labels" directory
            shutil.move(file_path, os.path.join(destination_dir, filename))
            print(f"Moved text file: {filename}")
        else:
            # Move the image file to the "images" directory
            shutil.move(file_path, os.path.join(destination_dir, filename))
            print(f"Moved image file: {filename}")

# Define the source directory containing the files
source_directory = 'coco_dataset/151'

# Define the destination directory for images and labels
destination_directory = 'coco_dataset_new'


# Split files into "images" and "labels" directories
split_files(source_directory, destination_directory)
split_files(source_directory, os.path.join(destination_directory, 'labels'))
