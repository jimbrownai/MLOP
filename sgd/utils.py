import matplotlib.pyplot as plt 
import torch
from dataloader import create_dataset,create_dataloaders
from simpleNN import SimpleNN
import torch.optim as optim
import torch.nn as nn
from trainer import evaluate_model

def plot_traning_results(results_dict):
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(15,5))

    for name, (losses,accuracies) in results_dict.items():
        ax1.plot(losses, label=f'{name} Loss')
        ax2.plot(accuracies, label = f'{name} Accuracy')

    ax1.set_title('Traning Loss Comparison')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    ax1.grid(True)

    ax2.set_title('Test Accuracy Comparison')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def save_model(model,filename):
    torch.save(model.state_dict(), filename)
    print(f"Model saved as {filename}")

def load_model(model,filename):
    model.load_state_dict(torch.load(filename))
    model.eval() 
    print(f"Model loaded from {filename}")

def hyperparameter_search():

    learning_rates = [0.001,0.01,0.1]
    momentum_values = [0.0,0.5,0.9]

    best_acc = 0
    best_params = {}

    X_train,X_test,y_train,y_test = create_dataset(n_samples=500,n_feactures=10,n_classes=2)
    train_loader,test_loader = create_dataloaders(X_train,X_test,y_train,y_test)

    for lr in learning_rates:
        for momentum in momentum_values:
            print(f"Testing lr={lr}, momentum={momentum}") 
            model = SimpleNN(10,32,2)
            optimizer = optim.SGD(model.parameters(),lr=lr,momentum=momentum)
            criterion = nn.CrossEntropyLoss()
        
            for epoch in range(10):
                model.train()
                for data,target in train_loader:
                    optimizer.zero_grad()
                    output = model(data)
                    loss = criterion(output,target)
                    loss.backward() 
                    optimizer.step()
            
            acc = evaluate_model(model, test_loader)
            print(f' Accuracy: {acc:.4f}')

            if acc> best_acc:
                best_acc = acc 
                best_params = {'lr':lr, 'momentum': momentum}
    print(f'\n Best parameters: {best_params}')
    print(f'Best accuracy: {best_acc:.4f}')
    
        
