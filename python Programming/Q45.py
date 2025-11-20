print("Om Nimmalwar")
class EmployeeNotFound(Exception):
    pass


employees = ["Om", "Sahil", "Amit", "Sanjay", "Manav"]

try:
    name = input("Enter employee name: ")

    
    found = False
    for emp in employees:
        if emp == name:
            found = True
            break

    if not found:
        raise EmployeeNotFound("Employee not found in the list!")

    print("Employee found:", name)

except EmployeeNotFound as e:
    print(e)
