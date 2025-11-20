print("Om Nimmalwar")
class MyString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        
        print(self.s.upper())



obj = MyString()
obj.getString()
obj.printString()
