print("Sahil Tapas")
people = []
n = int(input("Enter number of entries: "))

for i in range(n):   # using i instead of _
    name, age, height = input("Enter name, age, height: ").split(',')
    people.append((name, int(age), int(height)))

people.sort(key=lambda x: (x[0], x[1], x[2]))
print(people)