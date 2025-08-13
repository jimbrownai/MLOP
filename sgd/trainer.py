import torch 
import torch.nn as nn 
from simpleSgd import SimpleSGD
from sgdMomentum import SGDWithMomentum

def evaluate_model(model,test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            _, predicted = torch.max(output.data,1)
            total += target.size(0)
            correct += (predicted==target).sum().item()
    return correct/total

def train(model,optimizer,train_loader,test_loader,epochs =50):
    optimizer = optimizer
    criterion = nn.CrossEntropyLoss() 
    train_losses = [] 
    test_accuracies = [] 

    for epoch in range(epochs):
        model.train()
        epoch_loss = 0.0

        for batch_idx, (data,target) in enumerate(train_loader):
            optimizer.zero_grad(model)

            outputs = model(data)
            loss = criterion(outputs,target)

            loss.backward() 
            if isinstance(optimizer,SimpleSGD) or isinstance(optimizer, SGDWithMomentum):
                optimizer.step(model)
            else:
                optimizer.step()

            epoch_loss += loss.item() 
        
        test_acc = evaluate_model(model,test_loader)
        test_accuracies.append(test_acc)

        avg_train_loss = epoch_loss/len(train_loader)
        train_losses.append(avg_train_loss)

        if epoch % 10 == 0:
            print(f'Epoch {epoch:3d}: Loss = {train_losses[-1]:.4f}, Test Acc = {test_acc:.4f}')
        
    return train_losses,test_accuracies


    