#11. Write a python code to find duplicate elements in an array 
print("Submitted By : OM NIMMALWAR")
print("Roll No: MC25058")
a = [1,2,3,4,4,5,3,2,7,8,9]
print("Array:")
print(a)
b = []
count = 0
for i in range(len(a)):
    if a[i] not in b:
        b += [a[i]]
for j in range(len(b)):
    for k in range(len(a)):
        if b[j] == a[k]:
            count += 1
    if count > 1:
        print(f"{b[j]} is Duplicate")
    count = 0