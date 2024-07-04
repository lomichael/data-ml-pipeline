import torch
import torch.optim as optim
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
dataloader = DataLoader(dataset, batch_size=10)

model = SimpleModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    for batch in dataloader:
        inputs, targets = batch
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

torch.save(model.state_dict(), '/usr/local/model/model.pth')

