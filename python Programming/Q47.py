print("Om Nimmalwar")
class PasswordLengthError(Exception):
    pass

try:
    password = input("Enter your password: ")

    min_len = 6
    max_len = 12

    length = 0
    
    for ch in password:
        length += 1

   
    if length < min_len or length > max_len:
        raise PasswordLengthError(
            f"Password length must be between {min_len} and {max_len} characters."
        )

    print("Password length is valid.")

except PasswordLengthError as e:
    print("Error:", e)
