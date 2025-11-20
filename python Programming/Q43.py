print("Om Nimmalwar")
import re

pattern = r'^[789][0-9]{9}$'

mobile = input("Enter Mobile Number: ")

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
