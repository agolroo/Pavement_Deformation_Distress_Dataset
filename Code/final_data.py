import os
import random
import shutil

# Set up directories
os.chdir(r"..\data")
os.makedirs('train/images', exist_ok=True)
os.makedirs('train/labels', exist_ok=True)
os.makedirs('valid/images', exist_ok=True)
os.makedirs('valid/labels', exist_ok=True)
os.makedirs('test/images', exist_ok=True)
os.makedirs('test/labels', exist_ok=True)

# Get a list of all the non-zero label filenames
label_filenames = [f for f in os.listdir('labels') if os.path.getsize(os.path.join('labels', f)) > 0]

# Shuffle the list of label filenames
random.shuffle(label_filenames)

# Calculate the number of files for each set
num_files = len(label_filenames)
num_train = int(num_files * 0.8)
num_valid = int(num_files * 0.1)
num_test = num_files - num_train - num_valid

# Loop through the shuffled list of label filenames and copy files to train/valid/test directories
for i, filename in enumerate(label_filenames):
    if i < num_train:
        set_dir = 'train'
    elif i < num_train + num_valid:
        set_dir = 'valid'
    else:
        set_dir = 'test'

    shutil.copy(os.path.join('images', filename[:-4] + '.jpg'), os.path.join(set_dir, 'images'))
    shutil.copy(os.path.join('labels', filename), os.path.join(set_dir, 'labels'))






# Get a list of all the zero label filenames
label_filenames_zero = [f for f in os.listdir('labels') if os.path.getsize(os.path.join('labels', f)) == 0]

# Shuffle the list of label filenames
random.shuffle(label_filenames_zero)

# Calculate the number of files for each set
num_files_zero = len(label_filenames_zero)
num_train_zero = int(num_files_zero * 0.8)
num_valid_zero = int(num_files_zero * 0.1)
num_test_zero = num_files_zero - num_train_zero - num_valid_zero

# Loop through the shuffled list of label filenames and copy files to train/valid/test directories
for i, filename in enumerate(label_filenames_zero):
    if i < num_train_zero:
        set_dir = 'train'
    elif i < num_train_zero + num_valid_zero:
        set_dir = 'valid'
    else:
        set_dir = 'test'

    shutil.copy(os.path.join('images', filename[:-4] + '.jpg'), os.path.join(set_dir, 'images'))
    shutil.copy(os.path.join('labels', filename), os.path.join(set_dir, 'labels'))

