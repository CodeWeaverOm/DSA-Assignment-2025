print("Om Nimmalwar")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = [3, 4, 5, 6, 7, 8]
for num in lst:
    print(num, "->", is_prime(num))
