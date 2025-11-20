print("Om Nimmalwar")
password = input("Enter Password: ")

lower = False
upper = False
digit = False
special = False


for ch in password:
   
    if 'a' <= ch <= 'z':
        lower = True
    
    elif 'A' <= ch <= 'Z':
        upper = True
    
    elif '0' <= ch <= '9':
        digit = True
    
    elif ch == '$' or ch == '#' or ch == '@':
        special = True


length_ok = 6 <= len(password) <= 16


if lower and upper and digit and special and length_ok:
    print("Password is Valid")
else:
    print("Password is Invalid")
