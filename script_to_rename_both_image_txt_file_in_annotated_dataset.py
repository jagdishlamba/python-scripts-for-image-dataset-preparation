# script to rename both jpg file nad txt file with counting name
import os

folder_path =  r'151'
new_path = "1512"
try:
    os.mkdir(new_path)
except:
    print("already exists")

count = 7210

for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        image_file_path = os.path.join(folder_path, file_name)
        text_file_name = os.path.splitext(file_name)[0] + ".txt"
        text_file_path = os.path.join(folder_path, text_file_name)

        if os.path.isfile(text_file_path):
            new_image_file_name = f"{count}.jpg"
            new_text_file_name = f"{count}.txt"
            
            new_image_file_path = os.path.join(new_path, new_image_file_name)
            new_text_file_path = os.path.join(new_path, new_text_file_name)

            # Rename image file
            os.rename(image_file_path, new_image_file_path)
            # Rename text file
            os.rename(text_file_path, new_text_file_path)

            count += 1
            print(f"Renamed files: {file_name} and {text_file_name} to {new_image_file_name} and {new_text_file_name}")

