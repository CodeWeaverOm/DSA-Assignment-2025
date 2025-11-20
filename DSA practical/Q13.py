#Que13. Write a python code to generate Fibonacci series up to 5 number using array elements
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a = [1,2] 
print("Fibinacci Start from :")
print(a)
for i in range(2, 5):  
    next_num = a[i-1] + a[i-2]
    a += [next_num]
print("Fibonacci Series (5 numbers):", a)
