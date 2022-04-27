import json


f = open("parameters.json")
s = f.read()
y = json.loads(s)
print(y)