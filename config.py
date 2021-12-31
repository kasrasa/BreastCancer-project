import os

# path to the dataset
input_dataset = "datasets/original"

# base path that we will build for each type of data
base_path = "datasets/idc"

# path to each forlder
Train_path = os.path.sep.join([base_path,"training"])
Val_path = os.path.sep.join([base_path,"validation"])
Test_path = os.path.sep.join([base_path,"testing"])

# train, test, validation split ratio
Train_split = 0.8
Val_split = 0.1

