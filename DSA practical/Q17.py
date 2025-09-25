#Que17. Write a python code for matrix subtraction. 
print("Submitted By : OM NIMMALWAR")
print("Roll No: MC25058")
a = [[5, 9], [4, 3]]
b = [[3, 6], [3, 2]]
c = []
for i in range(len(a)):
    temp = []
    for j in range(len(a[0])):
        temp += [a[i][j] - b[i][j]]
    c += [temp]
print("Matrix A :", a)
print("Matrix B :", b)
print("Subtraction of Matrices :", c)