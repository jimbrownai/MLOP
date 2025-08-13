import torch 
import torch.nn as nn 
import torch.nn.functional as F 

class SimpleNN(nn.Module):

    def __init__(self, input_size,hidden_size,num_classes):
        super(SimpleNN,self).__init__()
        self.fc1 = nn.Linear(input_size,hidden_size)
        self.fc2 = nn.Linear(hidden_size,hidden_size)
        self.fc3 = nn.Linear(hidden_size,num_classes)
        self.dropout = nn.Dropout(0.2)

    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x 
