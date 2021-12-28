import os

input_dataset = "datasets/original"

base_path = "datasets/idc"

Train_path = os.path.sep.join([base_path,"training"])
Val_path = os.path.sep.join([base_path,"validation"])
Test_path = os.path.sep.join([base_path,"testing"])

Train_split = 0.8
Val_split = 0.1

