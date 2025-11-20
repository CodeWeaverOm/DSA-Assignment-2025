print("Om Nimmalwar")
def divide():
    return 5 / 0   
try:
    result = divide()
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
