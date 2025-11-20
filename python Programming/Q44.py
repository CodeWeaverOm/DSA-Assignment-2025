print("Om Nimmalwar")
import re

pattern = r'^[a-k][0369][a-zA-Z0-9#]*$'

identifier = input("Enter Identifier: ")

if re.match(pattern, identifier):
    print("Valid PIBM Identifier")
else:
    print("Invalid PIBM Identifier")
