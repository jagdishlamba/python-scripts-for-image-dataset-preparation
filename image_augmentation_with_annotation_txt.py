'''
    This script will rotate the annoatated image to 90, 180, 270 degree along with annotated txt file to reduce human effort of annotating all augmentated images again. 
'''

import os
import cv2
import numpy as np

def rotate_image_and_annotations(image_path, annotation_path, rotation_angle, output_folder):
    # Load the image and annotation
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    annotations = []
    with open(annotation_path, 'r') as f:
        annotations = f.readlines()

    # Rotate the image
    rotated_image = np.rot90(image, rotation_angle // 90)

    # Update annotations
    rotated_annotations = []
    for annotation in annotations:
        parts = annotation.strip().split()
        class_label = parts[0]
        x, y, w, h = map(float, parts[1:])
        
        if rotation_angle == 90:
            new_x = y
            new_y = 1.0 - (x + w)
            new_w = h
            new_h = w
        elif rotation_angle == 180:
            new_x = 1.0 - (x + w)
            new_y = 1.0 - (y + h)
            new_w = w
            new_h = h
        elif rotation_angle == 270:
            new_x = 1.0 - (y + h)
            new_y = x
            new_w = h
            new_h = w
        
        rotated_annotations.append(f'{class_label} {new_x:.6f} {new_y:.6f} {new_w:.6f} {new_h:.6f}')
    
    # Save the rotated image
    image_name = os.path.basename(image_path)
    rotated_image_path = f'rotated_{rotation_angle}_degree_{image_name}'
    cv2.imwrite(output_folder + "/" + rotated_image_path, rotated_image)

    # Save the rotated annotations
    annotation_name = os.path.basename(annotation_path)
    rotated_annotation_path = f'{output_folder}/rotated_{rotation_angle}_degree_{annotation_name}'
    with open(rotated_annotation_path, 'w') as f:
        for annotation in rotated_annotations:
            f.write(annotation + '\n')

    print(f'Image {image_name} rotated by {rotation_angle} degrees and annotations updated.')

# Folder containing images and annotation files
input_folder = 'sample'

output_folder = 'rotated_image'

try:
    os.mkdir(output_folder)
except Exception as e:
    print("folder already exists")

# Iterate through files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image_path = os.path.join(input_folder, filename)
        annotation_filename = os.path.splitext(filename)[0] + '.txt'
        annotation_path = os.path.join(input_folder, annotation_filename)
        
        if os.path.isfile(annotation_path):
            rotate_image_and_annotations(image_path, annotation_path, 90, output_folder)
            rotate_image_and_annotations(image_path, annotation_path, 180, output_folder)
            rotate_image_and_annotations(image_path, annotation_path, 270, output_folder)
