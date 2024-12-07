import os
# specify the folder path
train_directory_labels = r'..\train\labels'
test_directory_labels = r'..\test\labels'
valid_directory_labels = r'..\valid\labels'

# get a list of all label files in the folder
label_files_train = [l for l in os.listdir(train_directory_labels)]
label_files_valid = [l for l in os.listdir(valid_directory_labels)]
label_files_test = [l for l in os.listdir(test_directory_labels)]

shovingclass=[4,5]
bumpsagclass=[0,1]
shoving=0
bumpsag=0
shcount=0
bscount=0

#train

for i in range(0, len(label_files_train)):
    filepath=os.path.join(train_directory_labels, label_files_train[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass:
                    shoving=1
                elif first_col_value in bumpsagclass:
                    bumpsag=1
    shcount=shcount+shoving
    bscount=bscount+bumpsag
    shoving=bumpsag=0

#valid

for i in range(0, len(label_files_valid)):
    filepath=os.path.join(valid_directory_labels, label_files_valid[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass:
                    shoving=1
                elif first_col_value in bumpsagclass:
                    bumpsag=1
    shcount=shcount+shoving
    bscount=bscount+bumpsag
    shoving=bumpsag=0

#test

for i in range(0, len(label_files_test)):
    filepath=os.path.join(test_directory_labels, label_files_test[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass:
                    shoving=1
                elif first_col_value in bumpsagclass:
                    bumpsag=1
    shcount=shcount+shoving
    bscount=bscount+bumpsag
    shoving=bumpsag=0

print(f"shoving image number: {shcount}")
print(f"shoving image number: {bscount}")

#count instances

sh=0
bs=0

#train

for i in range(0, len(label_files_train)):
    filepath=os.path.join(train_directory_labels, label_files_train[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass:
                    sh=sh+1
                elif first_col_value in bumpsagclass:
                    bs=bs+1

#valid

for i in range(0, len(label_files_valid)):
    filepath=os.path.join(valid_directory_labels, label_files_valid[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass:
                    sh=sh+1
                elif first_col_value in bumpsagclass:
                    bs=bs+1

#test

for i in range(0, len(label_files_test)):
    filepath=os.path.join(test_directory_labels, label_files_test[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass:
                    sh=sh+1
                elif first_col_value in bumpsagclass:
                    bs=bs+1

print(f"shoving instances number: {sh}")
print(f"shoving instances number: {bs}")

# count classes
shovingclass1=[4]
shovingclass2=[5]
bumpsagclass1=[0]
bumpsagclass2=[1]
sh1=sh2=bs1=bs2=0
# train

for i in range(0, len(label_files_train)):
    filepath=os.path.join(train_directory_labels, label_files_train[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass1:
                    sh1=sh1+1
                elif first_col_value in shovingclass2:
                    sh2=sh2+1
                elif first_col_value in bumpsagclass1:
                    bs1=bs1+1
                elif first_col_value in bumpsagclass2:
                    bs2=bs2+1

#valid

for i in range(0, len(label_files_valid)):
    filepath=os.path.join(valid_directory_labels, label_files_valid[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass1:
                    sh1=sh1+1
                elif first_col_value in shovingclass2:
                    sh2=sh2+1
                elif first_col_value in bumpsagclass1:
                    bs1=bs1+1
                elif first_col_value in bumpsagclass2:
                    bs2=bs2+1

#test

for i in range(0, len(label_files_test)):
    filepath=os.path.join(test_directory_labels, label_files_test[i])
    if os.path.getsize(filepath) != 0:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                # Split the line by space and check the first column value
                first_col_value = int(lines[i].split()[0])
                if first_col_value in shovingclass1:
                    sh1=sh1+1
                elif first_col_value in shovingclass2:
                    sh2=sh2+1
                elif first_col_value in bumpsagclass1:
                    bs1=bs1+1
                elif first_col_value in bumpsagclass2:
                    bs2=bs2+1

print(f"shoving-S1 instances number: {sh1}")
print(f"shoving-S2 instances number: {sh2}")
print(f"BumpSag-S1 instances number: {bs1}")
print(f"BumpSag-S2 instances number: {bs2}")