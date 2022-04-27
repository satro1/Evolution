import json


def parse_json(file):
    f = open(file)
    s = f.read()
    return json.loads(s)