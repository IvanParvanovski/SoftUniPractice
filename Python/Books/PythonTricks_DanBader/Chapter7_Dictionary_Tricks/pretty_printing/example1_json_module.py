import json

mapping = {'a': 23, 'b': 42, 'c': 0xc0fffee}

print(json.dumps(mapping, indent=4, sort_keys=True))
