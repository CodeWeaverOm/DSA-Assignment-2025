print("Om Nimmalwar")
class InvalidAgeException(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    
    if age < 0:
        raise InvalidAgeException("Age cannot be negative!")

    
    if age < 18:
        raise InvalidAgeException("Not eligible for voting!")

    print("You are eligible to vote.")

except InvalidAgeException as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid number for age.")
