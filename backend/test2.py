import json

# Opening JSON file
f = open('../data/users.json')
data = json.load(f)

print(data["1"])