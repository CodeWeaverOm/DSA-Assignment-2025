print("Sahil Tapas")
text = input("Enter text: ")
words = text.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

for key in sorted(freq.keys()):
    print(f"{key}: {freq[key]}")
