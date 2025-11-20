print("Om Nimmalwar")
class NotEligibleForDrivingLicense(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise NotEligibleForDrivingLicense("NotEligibleForDrivingLicense")

    print("You are eligible for a driving license.")

except NotEligibleForDrivingLicense as e:
    print("Exception:", e)

except ValueError:
    print("Invalid input! Please enter a valid number.")
