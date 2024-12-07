import os
import random

# Set the path to the directory containing the images and labels subfolders
folder_path = r"..\data"

# Get a list of all non-zero txt files and their corresponding image files
image_files = []
label_files = []
for filename in os.listdir(os.path.join(folder_path, "images")):
    if filename.endswith(".jpg"):
        # Check if the corresponding label file exists and has non-zero size
        label_path = os.path.join(folder_path, "labels", filename[:-4] + ".txt")
        if os.path.exists(label_path) and os.path.getsize(label_path) > 0:
            image_files.append(os.path.join(folder_path, "images", filename))
            label_files.append(label_path)

# Calculate the number of files to keep (1/9 of non-zero files)
num_to_keep = int( 1/9 * len(image_files))

# Get a list of all zero-size txt files and their corresponding image files
zero_image_files = []
zero_label_files = []
for filename in os.listdir(os.path.join(folder_path, "images")):
    if filename.endswith(".jpg"):
        # Check if the corresponding label file exists and has zero size
        label_path = os.path.join(folder_path, "labels", filename[:-4] + ".txt")
        if os.path.exists(label_path) and os.path.getsize(label_path) == 0:
            zero_image_files.append(os.path.join(folder_path, "images", filename))
            zero_label_files.append(label_path)

# Randomly select files to keep from the zero-size files
if len(zero_image_files) > num_to_keep:
    not_keep_indices = random.sample(range(len(zero_image_files)), (len(zero_image_files)-num_to_keep))
    zero_image_files = [zero_image_files[i] for i in not_keep_indices]
    zero_label_files = [zero_label_files[i] for i in not_keep_indices]

# Delete the files that are not kept
for image_file, label_file in zip(zero_image_files, zero_label_files):
    os.remove(image_file)
    os.remove(label_file)
