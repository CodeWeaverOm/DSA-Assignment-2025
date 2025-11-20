print("Sahil Tapas")
text = input("Enter string: ")
freq = {ch: text.count(ch) for ch in set(text)}
ascii_dict = {ch: ord(ch) for ch in set(text)}

print("Frequency dictionary:", freq)
print("ASCII dictionary:", ascii_dict)
