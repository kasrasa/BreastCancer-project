# BreastCancer-project

The dataset is setup using config.py and build-dataset.py.


The dataset used in this project is IDC (Invasive Ductal Carcinoma) with imbalanced data of benign and malignant breast cancer cases. The optimizers used are adagrad ,which adapts
the learning rate according to the frequency of appearance meaning that it will assign higher learning rate (larger update for the parameters) and smaller learning rate 
(smaller paramter updates), and adam which is a very common optimizer used in neural networks that computes adaptive learning rates for each parameters. 
Data augmentation and class weights are used to tackle the imbalance issue. Data is normalized and augmented by flipping, rotation, shifting and shearing. 

The results show the better performance of the model using adam optimizer in comparison with adagrad and achieved the accuracy of 83%. 

Details are included in the code as comments.
