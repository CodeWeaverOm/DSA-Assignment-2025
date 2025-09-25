#Que9. Write a python code to merge two arrays into one. 
print("Submitted By : OM NIMMALWAR")
print("Roll No: MC25058")
a = [1,2,3,4]
b = [5,6,7,8]
c = []
print("First Array :")
print(a)
print("Second Array :")
print(b)

for i in range(len(b)):
    a += [b[i]]
c = a

print("Combination of Both Arrays are :")
print(c)