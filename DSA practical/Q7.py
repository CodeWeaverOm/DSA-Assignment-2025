#Que7. Write a python code to count frequency of each element in the array. 
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a = [1,2,3,4,5,6,3,4,2,3,2,2,2,1,4,5,3,8,7]
b = []
count = 0
print("Array :")
print(a)
for i in range(len(a)):
    if a[i] not in b:
        b += [a[i]]
for j in range(len(b)):
    for k in range(len(a)):
        if b[j] == a[k]:
            count += 1
    print(f"{b[j]} occurs {count} times in array")
    count = 0