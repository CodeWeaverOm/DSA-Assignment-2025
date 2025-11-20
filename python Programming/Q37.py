print("Om Nimmalwar")
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    
    def get_price(self, quantity):
        

    
        discount = 0.0

        if quantity < 10:
            discount = 0.0
        else:
            if quantity < 100:
                discount = 0.10
            else:
                discount = 0.20

        cost = quantity * self.price * (1 - discount)
        return cost

    
    def make_purchase(self, quantity):
        
        if quantity > self.amount:
            print("Not enough stock available!")
            return False
        else:
            self.amount = self.amount - quantity
            print(quantity, "items purchased successfully.")
            print("Remaining stock:", self.amount)
            return True



name = input("Enter Product Name: ")
amount = int(input("Enter Stock Quantity: "))
price = float(input("Enter Price per Item: "))

product = Product(name, amount, price)

qty = int(input("\nEnter number of items to buy: "))

cost = product.get_price(qty)
print("Total Cost =", cost)

product.make_purchase(qty)
