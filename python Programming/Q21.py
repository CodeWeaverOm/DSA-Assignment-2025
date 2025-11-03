print("Om Nimmalwar")
people = []
n = int(input("Enter number of entries: "))

for _ in range(n):
    name, age, height = input("Enter name, age, height: ").split(',')
    people.append((name, int(age), int(height)))

people.sort(key=lambda x: (x[0], x[1], x[2]))
print(people)
