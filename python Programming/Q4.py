print("Sahil Tapas")
n = 5  
for i in range(1, n + 1):
    row = " ".join(chr(65 + j) for j in range(i))
    print(row.center(n * 2 - 1))
