# python image_augmentor.py --source source_foler --dest dest_folder
import os
import imgaug as ia
from imgaug import augmenters as iaa
from PIL import Image
import numpy as np
import argparse

def augment_dataset(input_folder, output_folder, num_augmented_images_per_original):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Define augmentation sequence
    seq = iaa.Sequential([
        iaa.Fliplr(1),

                
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255)),  # Add Gaussian noise with a scale of 0 to 0.05 times the maximum pixel value
        
        iaa.Multiply((0.8, 1.2)),  # brightness
        iaa.Affine(scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}),
        iaa.GammaContrast(gamma=(0.5, 2.0)),  # Apply gamma contrast adjustment with a gamma value randomly chosen between 0.5 and 2.0

    ])

    # Iterate through each image in the input folder
    for image_file in os.listdir(input_folder):
        image_path = os.path.join(input_folder, image_file)

        # Open image using PIL
        image = Image.open(image_path)

        # Convert PIL image to numpy array
        image_array = ia.imresize_single_image(np.array(image), (image.height, image.width))

        # Apply augmentation multiple times to create augmented images
        for i in range(num_augmented_images_per_original):
            # Apply augmentation
            augmented_image_array = seq.augment_image(image_array)

            # Convert augmented numpy array back to PIL image
            augmented_image = Image.fromarray(augmented_image_array)

            # Save augmented image
            augmented_image_path = os.path.join(output_folder, f"augmented_{image_file}_{i+1}.jpg")
            augmented_image.save(augmented_image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Image Augmentor',
                    description='this rogram augment the image dataset',
                    epilog='Check on Pypi for more options')
    
    parser.add_argument('-s', '--source', required =True, help="Enter the source folder")      # option that takes a value
    parser.add_argument('-d', '--dest', required =True, help="Enter the destination folder path")

    args = parser.parse_args()
    
    input_folder = args.source  # Specify the input folder containing original images
    output_folder = args.dest  # Specify the output folder to store augmented images
    num_augmented_images_per_original = 5  # Specify the number of augmented images to generate per original image

    augment_dataset(input_folder, output_folder, num_augmented_images_per_original)
