d = {'a': 1, 'b': 2, 'c': 3}

print(d.keys())         # 1. Get keys
print(d.values())       # 2. Get values
print(d.items())        # 3. Get key-value pairs
d.update({'d': 4})      # 4. Add new key-value
d.pop('b')              # 5. Remove by key
print(d)
