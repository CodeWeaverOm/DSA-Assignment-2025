print("Om Nimmalwar")
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(i, j)
