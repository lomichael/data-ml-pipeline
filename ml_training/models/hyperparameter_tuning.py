import torch
import optuna
from torch.utils.data import DataLoader, TensorDataset
from model import SimpleModel
import psycopg2
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="ml_pipeline",
    user="postgres",
    password="your_password"
)
query = "SELECT * FROM training_data"
df = pd.read_sql_query(query, conn)
conn.close()

# Convert dataframe to tensors
x = torch.tensor(df.drop('target', axis=1).values, dtype=torch.float32)
y = torch.tensor(df['target'].values, dtype=torch.float32).unsqueeze(1)

dataset = TensorDataset(x, y)

def objective(trial):
    lr = trial.suggest_float('lr', 1e-5, 1e-1, log=True)
    batch_size = trial.suggest_int('batch_size', 10, 100)

    dataloader = DataLoader(dataset, batch_size=batch_size)

    model = SimpleModel()
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)

    for epoch in range(10):  # Use fewer epochs for faster tuning
        for batch in dataloader:
            inputs, targets = batch
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

    return loss.item()

study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)
print(study.best_trial)

