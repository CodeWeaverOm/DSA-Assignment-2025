print("Om Nimmalwar")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14159
        return pi * self.radius * self.radius

    def perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius



r = float(input("Enter radius of circle: "))

c = Circle(r)

print("Area of circle =", c.area())
print("Perimeter of circle =", c.perimeter())
