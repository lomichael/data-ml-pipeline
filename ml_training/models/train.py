import torch
import torch.nn as nn
import torch.optim as optim
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

# Initialize and train the model
model = SimpleModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# Save the model
torch.save(model.state_dict(), 'simple_model.pth')

