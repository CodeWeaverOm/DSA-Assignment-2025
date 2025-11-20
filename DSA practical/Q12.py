#Que12. Write a python code to find the maximum and minimum element.
print("Submitted By : SAHIL TAPAS")
print("Roll NO : MC25082")
a = [19,6,4,79,5,56]
max = 0
min = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
print("Array:")
print(a)
print(f"Maximum Value of element in array :{max}")
print(f"Minmum Value Of elment in array is : {min}")