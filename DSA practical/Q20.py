#Que20. Write a python code to find the sum of diagonal elements. 
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a=[[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(len(a)):
    sum += a[i][i]

print("Array : ",a)

print(f"Sum Of Diagonal Element Of Array Is {sum}")