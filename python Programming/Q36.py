print("Om Nimmalwar")
class Investment:
    def __init__(self, principal, interest):
        self.principal = principal     
        self.interest = interest        

    def value_after(self, n):
        value = self.principal * ((1 + self.interest) ** n)
        return value


p = float(input("Enter Principal Amount: "))
i = float(input("Enter Interest Rate (e.g., 0.05 for 5%): "))
n = int(input("Enter Number of Years: "))

inv = Investment(p, i)
final_value = inv.value_after(n)

print("Value of Investment after", n, "years =", final_value)
