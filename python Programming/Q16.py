d = {'b': 3, 'a': 1, 'c': 2}

# Sort by key
print(dict(sorted(d.items())))

# Sort by value
print(dict(sorted(d.items(), key=lambda item: item[1])))
