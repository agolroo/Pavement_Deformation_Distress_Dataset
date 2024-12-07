import os
import cv2
import numpy as np

# Define the two classes to be flipped
class_0 = 0
class_1 = 1

# Define the input and output directories
input_dir = r"..\images"
label_dir = r"..\labels"
output_dir = r"..\validaugmentated"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all images and their corresponding labels
for file in os.listdir(input_dir):
    if file.endswith(".jpg") or file.endswith(".png"):
        # Load the image and its corresponding label
        image = cv2.imread(os.path.join(input_dir, file))
        label_file = os.path.splitext(file)[0] + ".txt"
        label_path = os.path.join(label_dir, label_file)
        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                lines = f.readlines()
            # Loop through all annotations in the label file
            for line in lines:
                # Extract the class label and coordinates
                class_label, x_min, y_min, x_max, y_max = line.strip().split()
                class_label = int(class_label)
                x_min = float(x_min)
                y_min = float(y_min)
                x_max = float(x_max)
                y_max = float(y_max)
                # Check if the class label matches one of the two classes to be flipped
                if class_label == class_0 or class_label == class_1:
                    # Flip the coordinates horizontally
                    new_x_min = 1.0 - x_max
                    new_x_max = 1.0 - x_min
                    # Write the flipped coordinates to the output label file
                    output_label_file = os.path.splitext(file)[0] + "_flipped.txt"
                    output_label_path = os.path.join(output_dir, output_label_file)
                    with open(output_label_path, 'a') as f:
                        f.write(f"{class_label} {new_x_min} {y_min} {new_x_max} {y_max}\n")
            # Flip the image horizontally
            flipped_image = cv2.flip(image, 1)
            # Save the flipped image
            output_image_file = os.path.splitext(file)[0] + "_flipped.jpg"
            output_image_path = os.path.join(output_dir, output_image_file)
            cv2.imwrite(output_image_path, flipped_image)


# specify the folder path
folder_path = r"..\validaugmentated"

# get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

# iterate over each image file
for image_file in image_files:
    # construct the corresponding txt file path
    txt_file = os.path.splitext(image_file)[0] + '.txt'
    txt_file_path = os.path.join(folder_path, txt_file)

    # check if the txt file exists
    if not os.path.exists(txt_file_path):
        # delete the image file if the corresponding txt file doesn't exist
        os.remove(os.path.join(folder_path, image_file))
        print(f"Deleted {image_file}")
