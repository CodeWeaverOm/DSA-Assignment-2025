s = input("Enter string: ")
count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)