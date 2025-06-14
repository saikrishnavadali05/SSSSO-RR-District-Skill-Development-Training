import json
data = {"name": "John", "age": 30}
with open('data.json', 'w') as f:
    json.dump(data, f)
