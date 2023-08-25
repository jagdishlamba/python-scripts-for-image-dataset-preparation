import os
import random
import shutil

def split_data(input_folder, output_train_folder, output_test_folder, split_ratio):
    # Create output folders if they don't exist
    os.makedirs(output_train_folder, exist_ok=True)
    os.makedirs(output_test_folder, exist_ok=True)

    # Get a list of all image files in the input folder
    image_files = [file for file in os.listdir(input_folder) if file.endswith(('.jpg', '.png', '.jpeg'))]

    # Calculate the number of files for the train and test sets based on the split ratio
    num_files = len(image_files)
    num_train = int(num_files * split_ratio)
    num_test = num_files - num_train

    # Randomly shuffle the list of image files
    random.shuffle(image_files)

    # Copy files to train and test folders
    for i, file in enumerate(image_files):
        src_image_path = os.path.join(input_folder, file)
        src_txt_path = os.path.join(input_folder, file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))

        if i < num_train:
            dst_image_path = os.path.join(output_train_folder, file)
            dst_txt_path = os.path.join(output_train_folder, file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))
        else:
            dst_image_path = os.path.join(output_test_folder, file)
            dst_txt_path = os.path.join(output_test_folder, file.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt'))

        shutil.copy(src_image_path, dst_image_path)
        shutil.copy(src_txt_path, dst_txt_path)

    print(f"Data split completed. Train set: {num_train} images, Test set: {num_test} images")

# Set paths and parameters
input_folder = 'new_augmented_dataset'
output_train_folder = 'train'
output_test_folder = 'val'
split_ratio = 0.8  # 80% for train, 20% for test

# Call the split_data function
split_data(input_folder, output_train_folder, output_test_folder, split_ratio)
