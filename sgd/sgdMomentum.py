import torch 

class SGDWithMomentum:
    def __init__(self,learning_rate=0.01,momentum=0.9):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.velocity = {}
    
    def step(self,model):
        with torch.no_grad():
            for name, param in model.named_parameters():
                if param.grad is not None:
                    if name not in self.velocity:
                        self.velocity[name] = torch.zeros_like(param.data)
                    
                    self.velocity[name] = (self.momentum * self.velocity[name] + self.learning_rate*param.grad)

                    param.data -= self.velocity[name]

    def zero_grad(self,model):
        for param in model.parameters():
            if param.grad is not None:
                param.grad.zero_()
            