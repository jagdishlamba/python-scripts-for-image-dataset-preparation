'''
    This script will rename the yolo class number in annotated txt file without changing bounding box points.
'''
import os

def change_class_label_folder(folder_path, old_label, new_label):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder_path, filename)
            change_class_label(filepath, old_label, new_label)

def change_class_label(filepath, old_label, new_label):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    with open(filepath, 'w') as file:
        for line in lines:
            line = line.strip().split(' ')
            if int(line[0]) == old_label:
                line[0] = str(new_label)
            line = ' '.join(line)
            file.write(line + '\n')

# Example usage
folder_path = r'frames pending annotation' # folder path containing images and txt files
old_label = 1  # The class label you want to change
new_label = 0  # The new class label you want to set

change_class_label_folder(folder_path, old_label, new_label)