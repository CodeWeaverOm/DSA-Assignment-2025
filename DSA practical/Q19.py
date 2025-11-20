#Que19. Write a python code to find the transpose of a matrix.
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i] = a[i][j]
print("Before Transpose :")
for k in a:
    for l in k:
        print(l,end = " ")
    print()
print("After transpose :")
for p in b:
    for q in p:
        print(q,end = " ")
    print()
