#Que1.Write a python program to Insert An element array
print("Submitted By : SAHIL TAPAS")
print("Roll Call : MC25082")
a = [1,2,7,8,6,5]
print("before insert :")
print(a)
a = a + [0]
pos = 2
element = 100
for i in range (len(a)-1,pos-1,-1):
    a[i] = a[i-1]
a[pos-1]=element
print("After insert : ")
print(a)
