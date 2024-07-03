FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y redis-server

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["redis-server", "--daemonize", "yes"] && ["python", "api/app.py"]

