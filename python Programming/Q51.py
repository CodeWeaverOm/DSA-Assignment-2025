print("Om Nimmalwar")
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

   
    if num < 0:
        raise NegativeNumberError("Negative numbers cannot be prime!")

    
    if num == 0 or num == 1:
        print(num, "is NOT a prime number.")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, "is a PRIME number.")
        else:
            print(num, "is NOT a prime number.")

except NegativeNumberError as e:
    print("Error:", e)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
