import os

# Define the directory containing the txt files
directory = r'..\data\test\labels'

# Define the allowed values for the first column
allowed_values = [0, 1, 4, 5]

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        
        # Open the file and loop through each line
        with open(filepath, 'r') as file:
            for line in file:
                # Split the line by space and check the first column value
                first_col_value = int(line.split()[0])
                if first_col_value not in allowed_values:
                    print(filename)
                    break
