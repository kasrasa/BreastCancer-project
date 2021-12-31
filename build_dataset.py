from genericpath import isdir
import config
from imutils import paths
import random, shutil, os

# reading image paths and shuffling them
original_paths = list(paths.list_images(config.input_dataset)) #making original paths to the images
random.seed(7)
random.shuffle(original_paths) # shuffles the image paths

# calculating and indexing the training and test paths
index = int(len(original_paths)*config.Train_split)
train_paths = original_paths[:index]
test_paths = original_paths[index:]

# calculating and indexing the validation paths
index = int(len(train_paths)*config.Val_split)
val_paths = train_paths[:index]
train_paths = train_paths[index:]

# list of tuples with info about trainging,validation and test sets
datasets = [("training",train_paths,config.Train_path),
            ("validation",val_paths,config.Val_path),
            ("testing",test_paths,config.Test_path)]

# Create directories for train,test and validation set based on their settype(training,testing or validation)
for (setType,original_paths,base_path) in datasets:
    print(f'Building {setType} set')

    if not os.path.exists(base_path):
        print(f'Building directory {base_path}')
        os.makedirs(base_path)

    for path in original_paths:
        file = path.split(os.path.sep)[-1] # filename
        label=file[-5:-4] # extract labels

        label_path = os.path.sep.join([base_path,label])
        if not os.path.exists(label_path):
            print(f'Building directory {label_path}')
            os.makedirs(label_path)

        new_path = os.path.sep.join([label_path,file])
        shutil.copy2(path,new_path)



