import torch
from model import SimpleModel

def load_model(path='model.pth'):
    model = SimpleModel(input_size=10, hidden_size=20, output_size=1)
    model.load_state_dict(torch.load(path))
    return model

