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
label_files_train = [l for l in os.listdir(train_directory_labels)]
label_files_valid = [l for l in os.listdir(valid_directory_labels)]
label_files_test = [l for l in os.listdir(test_directory_labels)]

#train
zerolabels=0
nonzerolabels=0
deletedfiles=0
for i in range(0, len(label_files_train)):
    if os.path.getsize(os.path.join(train_directory_labels, label_files_train[i])) == 0:
        zerolabels=zerolabels+1
    else:
        nonzerolabels=nonzerolabels+1

for l in os.listdir(train_directory_labels):
    if os.path.getsize(os.path.join(train_directory_labels, l)) == 0 and deletedfiles<=zerolabels-nonzerolabels/9:
        os.remove(os.path.join(train_directory_images, os.path.splitext(l)[0] + ".jpg"))
        print(f"Deleted {l}")
        os.remove(os.path.join(train_directory_labels, l))
        deletedfiles=deletedfiles+1

#valid
zerolabels=0
nonzerolabels=0
deletedfiles=0
for i in range(0, len(label_files_valid)):
    if os.path.getsize(os.path.join(valid_directory_labels, label_files_valid[i])) == 0:
        zerolabels=zerolabels+1
    else:
        nonzerolabels=nonzerolabels+1

for l in os.listdir(valid_directory_labels):
    if os.path.getsize(os.path.join(valid_directory_labels, l)) == 0 and deletedfiles<=zerolabels-nonzerolabels/9:
        os.remove(os.path.join(valid_directory_images, os.path.splitext(l)[0] + ".jpg"))
        print(f"Deleted {l}")
        os.remove(os.path.join(valid_directory_labels, l))
        deletedfiles=deletedfiles+1

#test
zerolabels=0
nonzerolabels=0
deletedfiles=0
for i in range(0, len(label_files_test)):
    if os.path.getsize(os.path.join(test_directory_labels, label_files_test[i])) == 0:
        zerolabels=zerolabels+1
    else:
        nonzerolabels=nonzerolabels+1

for l in os.listdir(test_directory_labels):
    if os.path.getsize(os.path.join(test_directory_labels, l)) == 0 and deletedfiles<=zerolabels-nonzerolabels/9:
        os.remove(os.path.join(test_directory_images, os.path.splitext(l)[0] + ".jpg"))
        print(f"Deleted {l}")
        os.remove(os.path.join(test_directory_labels, l))
        deletedfiles=deletedfiles+1