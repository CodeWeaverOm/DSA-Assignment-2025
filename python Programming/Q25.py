print("Om Nimmalwar")
def dups(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

print(dups([1, 2, 3, 2, 4, 1, 5]))
