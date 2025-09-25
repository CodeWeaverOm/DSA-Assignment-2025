#Que10. Write a Program to find common elements from 2 arrays. 
print("Submitted By : OM NIMMALWAR")
print("Roll No: MC25058")
a = [1,2,4,5,6,7,8,3]
b = [3,5,10,6,11,8]
c = []
small = []
large = []
if len(a) >= len(b):
    large = a
    small = b
else:
    large = b
    small = a
for i in range(len(small)):
    for j in range(len(large)):
        if small[i] == large[j]:
            c += [small[i]]
print("First Array :")
print(a)
print("Second Array :")
print(b)
print("Unique Element from Both Arrays are :")
print(c)