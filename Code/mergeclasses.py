import os

# Define the folder containing the txt files
folder_path = r'..\labels'

# Define the search and replace values
search_values = ['1', '5']
replace_values = ['0', '4']

# Loop through all txt files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        # Open the file
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            # Read the file contents into a list
            file_contents = file.readlines()
        
        # Loop through the rows in the file
        for i, row in enumerate(file_contents):
            # Split the row into columns
            columns = row.split(' ')
            
            # Check if the first column matches a search value
            if columns[0] in search_values:
                # Replace the first column with the corresponding replace value
                j = search_values.index(columns[0])
                columns[0] = replace_values[j]
                
                # Join the columns back into a row
                file_contents[i] = ' '.join(columns)
        
        # Save the modified file
        with open(file_path, 'w') as file:
            file.writelines(file_contents)
