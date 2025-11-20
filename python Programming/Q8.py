s = input("Enter a string of length 10: ")

if len(s) != 10:
    print("String must be of length 10")
else:
    found = False
    for i in range(len(s) - 4):
        if s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
            found = True
            break
    print(found)
