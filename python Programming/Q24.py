print("Om Nimmalwar")
name = input("Enter name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks (%): "))

if 17 <= age <= 21 and marks >= 80:
    print(name, "is eligible for loan.")
else:
    print(name, "is not eligible for loan.")
