#Que 4. Write a program to count elements in array 
print("Submitted By : OM NIMMALWAR")
print("Roll No : MC25058")
a = [1,2,3,4,5,6,8,2]
count = 0
print("Array:")
print(a)
for i in a:
    if i>=0:
        count += 1
print(f"Number of elemnet in array :{count}")