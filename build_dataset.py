from genericpath import isdir
import config
from imutils import paths
import random, shutil, os

# reading image paths and shuffling them
original_paths = list(paths.list_images(config.input_dataset))
random.seed(7)
random.shuffle(original_paths) # shuffles the image paths

index = int(len(original_paths)*config.Train_split)
train_paths = original_paths[:index]
test_paths = original_paths[index:]

index = int(len(train_paths)*config.Val_split)
val_paths = train_paths[:index]
train_paths = train_paths[index:]

datasets = [("training",train_paths,config.Train_path),
            ("validation",val_paths,config.Val_path),
            ("testing",test_paths,config.Test_path)]

for (setType,original_paths,base_path) in datasets:
    print(f'Building {setType} set')

    if not os.path.exists(base_path):
        print(f'Building directory {base_path}')
        os.mkdir(base_path)

    for path in original_paths:
        file = path.split(os.path.sep)[-1]
        label=file[-5:-4]

        label_path = os.path.sep.join([base_path,label])
        if not os.path.exists(label_path):
            print(f'Building directory {label_path}')
            os.mkdir(label_path)

            new_path = os.path.sep.join([label_path,file])
            shutil.copy2(input_path,new_path)



