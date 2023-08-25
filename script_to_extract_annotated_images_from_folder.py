# script to extract images.png having image.txt file from any folder
import os
import shutil

source_folder = "images"
destination_folder = "151"

try:
	os.mkdir(destination_folder)
except:
	print(" Destination folder already exists")

for file_name in os.listdir(source_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        image_file_path = os.path.join(source_folder, file_name)
        text_file_name = os.path.splitext(file_name)[0] + ".txt"
        text_file_path = os.path.join(source_folder, text_file_name)

        if os.path.isfile(text_file_path):
            # Move image file
            shutil.move(image_file_path, os.path.join(destination_folder, file_name))
            # Move text file
            shutil.move(text_file_path, os.path.join(destination_folder, text_file_name))
            print(f"Moved files: {file_name} and {text_file_name}")