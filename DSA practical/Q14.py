#Que14. Write a program to reverse the array 
print("Submitted By : OM NIMMALWAR")
print("Roll No: MC25058")
a = [2,3,4,5,6,7]
b = []
print("Array Before Reverse :")
print(a)
for i in range(len(a)-1,-1,-1):
    b += [a[i]]
a = b
print("Array After Reverse :")
print(a)
