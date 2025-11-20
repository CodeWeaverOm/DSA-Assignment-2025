#Que3. Write a python code to search element in array(linear search)
print("Submitted By : SAHIL TAPAS")
print("Roll Call : MC25082")
a = [1,2,3,4,5,6,7]
element = int(input("enter element to search : "))
find = False
for i in range(len(a)):
  if a[i] == element:
      print(f"Element {element} founded on position {a[i]}")
      find = True
      break
if find == False:
      print(f"Element {element} not founded")