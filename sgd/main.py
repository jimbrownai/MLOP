import torch 
import numpy as np
from dataloader import create_dataset,create_dataloaders
from simpleNN import SimpleNN
from simpleSgd import SimpleSGD
from sgdMomentum import SGDWithMomentum
from trainer import train 
import time
from utils import plot_traning_results

def main():
    torch.manual_seed(42)
    np.random.seed(42)

    X_train,X_test,y_train,y_test = create_dataset(n_samples=1000,n_feactures=20,n_classes=3)
    train_loaders,test_loaders = create_dataloaders(X_train,X_test,y_train,y_test,batch_size=32)

    results = {}

    #Train with custom SGD
    model1 = SimpleNN(input_size=20,hidden_size=64,num_classes=3)
    start_time = time.time()
    optimizer = SimpleSGD(learning_rate=0.01)
    losses1,acc1 = train(model1,optimizer,train_loaders,test_loaders,epochs=50)
    time1 = time.time() - start_time
    results['Custom SGD'] = (losses1,acc1)
    print(f"Custom SGD training time: {time1:.2f}seconds\n")

    #Train with Pytorch SGD

    model2 = SimpleNN(input_size=20,hidden_size=64,num_classes=3)
    optimizer2 = torch.optim.SGD(
        model2.parameters(),
        lr=0.01,
        momentum=0.9
    )
    start_time = time.time()
    losses2, acc2 = train(model2,optimizer2,train_loaders,test_loaders,epochs=50)
    time2 = time.time() - start_time
    results['Pytorch SGD'] = (losses2,acc2)
    print(f"Pytorch SGD training time: {time2:.2f}seconds\n")

    #Train with Adam
    model3 = SimpleNN(input_size=20,hidden_size=64,num_classes=3)
    optimizer3 = torch.optim.Adam(
        model3.parameters(),
        lr=0.001,
        betas=(0.9,0.999),
        eps=1e-8,
        weight_decay=0.01
    ) 
    start_time = time.time() 
    losses3,acc3 = train(model3,optimizer3,train_loaders,test_loaders,epochs=50)
    time3 = time.time() - start_time
    results['Adam Optimizer'] = (losses3,acc3)
    print(f"Adam training time: {time3:.2f}seconds\n")
    
    

    #Train with custom SGDMomentum
    model4 = SimpleNN(input_size=20,hidden_size=64,num_classes=3)
    start_time = time.time()
    optimizer4 = SGDWithMomentum()
    losses4,acc4 = train(model4,optimizer4,train_loaders,test_loaders,epochs=50)
    time4 = time.time() - start_time
    results['Custom SGD With Momentum'] = (losses4,acc4)
    print(f"Custom SGD Momentum training time: {time4:.2f}seconds\n")

    
    plot_traning_results(results_dict=results)

if __name__ == '__main__':
    main()