import torch 
import torch.nn as nn 
from torch.utils.data import DataLoader,TensorDataset
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def create_dataset(n_samples=1000, n_feactures=20,n_classes=3):
    X,y = make_classification(
        n_samples=n_samples,
        n_features= n_feactures,
        n_classes=n_classes,
        n_redundant=0,
        n_informative=n_feactures,
        random_state=42
    )

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)
    y_train = torch.LongTensor(y_train)
    y_test = torch.LongTensor(y_test)

    return X_train,X_test,y_train,y_test

def create_dataloaders(X_train,X_test,y_train,y_test,batch_size=32):
    train_dataset = TensorDataset(X_train,y_train)
    test_dataset = TensorDataset(X_test,y_test)

    train_loader = DataLoader(train_dataset,batch_size=batch_size,shuffle=True)
    test_loader = DataLoader(test_dataset,batch_size=batch_size,shuffle=False)

    return train_loader,test_loader
