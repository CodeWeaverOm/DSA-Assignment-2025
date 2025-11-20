lst = [10, 15, 20, 25, 30]
in_range = True

for x in lst:
    if x < 10 or x > 30:
        in_range = False
        break

print(in_range)
