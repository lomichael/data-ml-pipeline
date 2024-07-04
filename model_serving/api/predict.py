import torch
from model import SimpleModel

model = SimpleModel()
model.load_state_dict(torch.load('/usr/local/model/model.pth'))
model.eval()

def predict(data):
    inputs = torch.tensor(data['inputs'])
    with torch.no_grad():
        outputs = model(inputs)
    return {'outputs': outputs.tolist()}

