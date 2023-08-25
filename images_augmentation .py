
# import os
# import cv2
# import numpy as np

# def rotate_image(image, angle):
#     height, width = image.shape[:2]
#     rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
#     rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
#     return rotated_image

# # Load the image
# image = cv2.imread('Image_for_Augmention/')

# # Create a folder to save the rotated images
# output_folder = 'output/90_rotation'
# os.makedirs(output_folder, exist_ok=True)
# output_folder1 = 'output/180_rotation'
# os.makedirs(output_folder1, exist_ok=True)
# output_folder2 = 'output/270_rotation'
# os.makedirs(output_folder2, exist_ok=True)

# # Rotate the image 0 to 90 degrees
# rotated_90 = rotate_image(image, 90)
# output_path_90 = os.path.join(output_folder, 'rotated_90.jpg')
# cv2.imwrite(output_path_90, rotated_90)

# # Rotate the image 90 to 180 degrees
# rotated_180 = rotate_image(image, 180)
# output_path_180 = os.path.join(output_folder1, 'rotated_180.jpg')
# cv2.imwrite(output_path_180, rotated_180)

# # Rotate the image 180 to 270 degrees
# rotated_270 = rotate_image(image, 270)
# output_path_270 = os.path.join(output_folder2, 'rotated_270.jpg')
# cv2.imwrite(output_path_270, rotated_270)


import os
import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Input folder containing the images
input_folder = 'Image_for_Augmention/'

# Output folder to save the rotated images
# output_folder = 'output/'
# os.makedirs(output_folder, exist_ok=True)

output_folder = 'output/90_rotation'
os.makedirs(output_folder, exist_ok=True)
output_folder_1 = 'output/180_rotation'
os.makedirs(output_folder_1, exist_ok=True)
output_folder_2 = 'output/270_rotation'
os.makedirs(output_folder_2, exist_ok=True)


# Iterate over the files in the input folder
for filename in os.listdir(input_folder):
    # Load the image
    image_path = os.path.join(input_folder, filename)
    image = cv2.imread(image_path)
    
    # Rotate the image 0 to 90 degrees
    rotated_90 = rotate_image(image, 90)
    output_path_90 = os.path.join(output_folder, 'rotated_90_' + filename)
    cv2.imwrite(output_path_90, rotated_90)

    # Rotate the image 90 to 180 degrees
    rotated_180 = rotate_image(image, 180)
    output_path_180 = os.path.join(output_folder_1, 'rotated_180_' + filename)
    cv2.imwrite(output_path_180, rotated_180)

    # Rotate the image 180 to 270 degrees
    rotated_270 = rotate_image(image, 270)
    output_path_270 = os.path.join(output_folder_2, 'rotated_270_' + filename)
    cv2.imwrite(output_path_270, rotated_270)
