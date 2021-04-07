import json
mapping = {'a': 23, 'b': 42, 'c': {1, 2, 3}}

print(json.dumps(mapping, indent=4, sort_keys=True))
