import torch

def save_model(model, path):
    torch.save(model.state_dict(), path)

# Usage
model = SimpleModel()
save_model(model, '/usr/local/model/model.pth')

