import os
# specify the folder path
train_directory_images = r'..\train\images'
test_directory_images = r'..\test\images'
valid_directory_images = r'..\valid\images'
train_directory_labels = r'..\train\labels'
test_directory_labels = r'..\test\labels'
valid_directory_labels = r'..\valid\labels'

# get a list of all image files in the folder
image_files_train = [f for f in os.listdir(train_directory_images)]
image_files_valid = [f for f in os.listdir(valid_directory_images)]
image_files_test = [f for f in os.listdir(test_directory_images)]

# iterate over each image file in train
for image_file in image_files_train:
    # construct the corresponding txt file path
    txt_file = os.path.splitext(image_file)[0] + '.txt'
    txt_file_path = os.path.join(train_directory_labels, txt_file)

    # check if the txt file exists
    if not os.path.exists(txt_file_path):
        # delete the image file if the corresponding txt file doesn't exist
        os.remove(os.path.join(train_directory_images, image_file))
        print(f"Deleted {image_file}")

# iterate over each image file in valid
for image_file in image_files_valid:
    # construct the corresponding txt file path
    txt_file = os.path.splitext(image_file)[0] + '.txt'
    txt_file_path = os.path.join(valid_directory_labels, txt_file)

    # check if the txt file exists
    if not os.path.exists(txt_file_path):
        # delete the image file if the corresponding txt file doesn't exist
        os.remove(os.path.join(valid_directory_images, image_file))
        print(f"Deleted {image_file}")

# iterate over each image file
for image_file in image_files_test:
    # construct the corresponding txt file path
    txt_file = os.path.splitext(image_file)[0] + '.txt'
    txt_file_path = os.path.join(test_directory_labels, txt_file)

    # check if the txt file exists
    if not os.path.exists(txt_file_path):
        # delete the image file if the corresponding txt file doesn't exist
        os.remove(os.path.join(test_directory_images, image_file))
        print(f"Deleted {image_file}")