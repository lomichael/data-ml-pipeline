import torch
from model import SimpleModel

def load_model(path):
    model = SimpleModel()
    model.load_state_dict(torch.load(path))
    return model

# Usage
model = load_model('/usr/local/model/model.pth')

