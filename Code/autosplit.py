print("creating raw data")
import os

# Set the path to the folders
image_folder = r'..\data\images'
text_folder = r'..\data\labels'

# Get the list of non-0KB text files
nonzero_text_files = []
for text_file in os.listdir(text_folder):
  if os.path.getsize(os.path.join(text_folder, text_file)) > 0:
    nonzero_text_files.append(text_file)

# Keep a number of 0KB text files and their corresponding image files equal to the number of non-0KB text files
num_to_keep = len(nonzero_text_files)//9
num_kept = 0
for text_file in os.listdir(text_folder):
  # Check if the text file is 0KB in size
  if os.path.getsize(os.path.join(text_folder, text_file)) == 0:
    # If the number of kept 0KB text files is less than the number of non-0KB text files,
    # keep the corresponding image file and increment the number of kept 0KB text files
    if num_kept < num_to_keep:
      print(f'Keeping {text_file}')
      num_kept += 1
    # Otherwise, delete the corresponding image file and text file
    else:
      image_file = os.path.join(image_folder, os.path.splitext(text_file)[0] + '.jpg')
      if os.path.exists(image_file):
        os.remove(image_file)
        print(f'Deleted {image_file}')
      os.remove(os.path.join(text_folder, text_file))
      print(f'Deleted {text_file}')
