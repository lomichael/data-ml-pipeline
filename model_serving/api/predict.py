import redis
import torch
from load_model import load_model

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

model = load_model()

def predict(data):
    # Generate a cache key based on input data
    cache_key = str(data)
    
    # Check if the prediction is already cached
    cached_result = redis_client.get(cache_key)
    if cached_result:
        return eval(cached_result)

    # If not cached, perform prediction
    with torch.no_grad():
        inputs = torch.tensor(data['inputs'])
        outputs = model(inputs)
        result = outputs.tolist()
    
    # Cache the result
    redis_client.set(cache_key, str(result))
    
    return result

