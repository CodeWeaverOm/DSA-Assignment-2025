#Que5. Write a program to delete element from array 
print("Submitted By : SAHIL TAPAS")
print("Roll Call : MC25082")

a = [1, 2, 3, 4, 5, 6, 7]
print("Before deleting :")
print(a)

element = int(input("Enter Element to delete: "))

pos = -1
for i in range(len(a)):
    if element == a[i]:
        pos = i
        break

if pos != -1:
    for j in range(pos, len(a) - 1):
        a[j] = a[j + 1]
    a.pop()
    print("After Deleting :")
    print(a)
else:
    print(f"{element} not found")
