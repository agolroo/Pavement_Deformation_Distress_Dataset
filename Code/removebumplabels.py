import os

# Define the directory containing the txt files
train_directory = r'..\train\labels'
test_directory = r'..\test\labels'
valid_directory = r'..\valid\labels'

# Define the allowed values for the first column
allowed_values = [4, 5]

# Loop through all files in the directory
for filename in os.listdir(train_directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(train_directory, filename)
        
        # Open the file and loop through each line
        with open(filepath, 'r+') as file:
            lines = file.readlines()
            file.truncate(0)
            file.seek(0)
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in allowed_values:
                    file.write(lines[i])
                else:
                    print(f"Deleted bump line in TRAIN {lines[i]}")   
# Loop through all files in the directory
for filename in os.listdir(valid_directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(valid_directory, filename)
        
        # Open the file and loop through each line
        with open(filepath, 'r+') as file:
            lines = file.readlines()
            file.truncate(0)
            file.seek(0)
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in allowed_values:
                    file.write(lines[i])
                else:
                    print(f"Deleted bump line in VALID {lines[i]}")   
# Loop through all files in the directory
for filename in os.listdir(test_directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(test_directory, filename)
        
        # Open the file and loop through each line
        with open(filepath, 'r+') as file:
            lines = file.readlines()
            file.truncate(0)
            file.seek(0)
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in allowed_values:
                    file.write(lines[i])
                else:
                    print(f"Deleted bump line in TEST {lines[i]}")   
