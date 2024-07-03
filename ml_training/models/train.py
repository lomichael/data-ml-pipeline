import torch
import torch.optim as optim
import torch.nn as nn
from model import SimpleModel
from torch.utils.data import DataLoader, TensorDataset

# Dummy data
X_train = torch.randn(100, 10)
y_train = torch.randn(100, 1)

train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

model = SimpleModel(input_size=10, hidden_size=20, output_size=1)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 10
for epoch in range(num_epochs):
    for inputs, targets in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')

