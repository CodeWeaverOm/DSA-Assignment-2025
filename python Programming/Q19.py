lst = [1, 2, 3, 4]

# Generate 2-element combinations
two = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        two.append((lst[i], lst[j]))

# Generate 3-element combinations
three = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
            three.append((lst[i], lst[j], lst[k]))

# Store in dictionary
result = {'Two_Digit': two, 'Three_Digit': three}

print(result)
