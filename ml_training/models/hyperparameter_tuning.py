import torch
import torch.nn as nn
import torch.optim as optim
import optuna
import psycopg2
import pandas as pd

# Define your PyTorch model architecture
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="ml_pipeline",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

# Fetch data from the database
query = "SELECT * FROM your_table;"
data = pd.read_sql_query(query, conn)

# Preprocess data
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Convert data to PyTorch tensors
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.float32)

# Define objective function for Optuna
def objective(trial):
    # Hyperparameters to tune
    lr = trial.suggest_loguniform('lr', 1e-5, 1e-1)
    hidden_size = trial.suggest_int('hidden_size', 10, 100)

    # Define model, criterion, and optimizer
    model = SimpleModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    # Train the model
    for epoch in range(50):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

    return loss.item()

# Optimize hyperparameters using Optuna
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)

print("Best hyperparameters: ", study.best_params)

