import torch 

class SimpleSGD:
    
    def __init__(self,learning_rate=0.01):
        self.learning_rate = learning_rate
    
    def zero_grad(self,model):
        for param in model.parameters():
            if param.grad is not None:
                param.grad.zero_()
    
    def step(self,model):
        with torch.no_grad():
            for param in model.parameters():
                if param is not None:
                    param.data -= self.learning_rate * param.grad
