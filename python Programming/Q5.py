print("Sahil Tapas")
result = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)
print("Numbers divisible by 7 but not multiple of 5:")
print(result)
num