#Que8. Write a python code to find the average / mean of array elements.
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a = [1,2,3,4,4,3,2,2,3]
sum = 0
count = 0
mean = 0
for i in a:
    sum += i
    count += 1
mean = sum/count
print("Array :")
print(a)
print(f"The Mean Of Array is : {mean}")