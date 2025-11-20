print("Om Nimmalwar")
email = input("Enter Email ID: ")

def validate_email(email):
   
    for ch in email:
        if ch == " ":
            return False

    
    if "@" not in email:
        return False

    
    count_at = 0
    for ch in email:
        if ch == "@":
            count_at += 1

    
    if count_at != 1:
        return False

    
    at_pos = 0
    i = 0
    for ch in email:
        if ch == "@":
            at_pos = i
            break
        i += 1

    
    if at_pos == 0:
        return False

    
    dot_pos = -1
    for j in range(at_pos + 1, len(email)):
        if email[j] == ".":
            dot_pos = j
            break

    if dot_pos == -1:
        return False

    
    if dot_pos == len(email) - 1:
        return False

    return True



if validate_email(email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
