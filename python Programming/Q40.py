print("Om Nimmalwar")
class Shape:
    def area(self):
       
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


s = Square(5)
print("Area of Square =", s.area())

sh = Shape()
print("Area of Shape =", sh.area())
