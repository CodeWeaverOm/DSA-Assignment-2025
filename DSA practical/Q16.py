#Que16. Write a python code for matrix addition. 
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a = [[1, 2], [4, 3]]
b = [[3, 6], [3, 2]]
c = []
for i in range(len(a)):
    temp = []
    for j in range(len(a[0])):
        temp += [a[i][j] + b[i][j]]
    c += [temp]
print("Matrix A :", a)
print("Matrix B :", b)
print("Addition of Matrices :", c)