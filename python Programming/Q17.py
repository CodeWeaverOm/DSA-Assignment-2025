print("Om Nimmalwar")
s = input("Enter string: ")
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
print(count)
