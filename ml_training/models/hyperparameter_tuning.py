import optuna
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from model import SimpleModel

def objective(trial):
    input_size = 10
    hidden_size = trial.suggest_int('hidden_size', 10, 50)
    output_size = 1
    lr = trial.suggest_loguniform('lr', 1e-5, 1e-1)
    
    model = SimpleModel(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # Dummy data
    X_train = torch.randn(100, 10)
    y_train = torch.randn(100, 1)
    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    
    for epoch in range(10):
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

    return loss.item()

study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=20)

print(f'Best hyperparameters: {study.best_params}')

