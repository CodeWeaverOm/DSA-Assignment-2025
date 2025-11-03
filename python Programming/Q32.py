print("Om Nimmalwar")
def how_many(d):
    return sum(len(v) for v in d.values())

def biggest(d):
    return max(d, key=lambda k: len(d[k]))

example = {
    'a': [1, 2],
    'b': [1, 2, 3, 4],
    'c': [10]
}

print("Total number of values:", how_many(example))
print("Key with largest list:", biggest(example))
