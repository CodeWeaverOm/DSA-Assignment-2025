print("Sahil Tapas")
num = int(input("Enter a number: "))
is_negative = num < 0
num_abs = abs(num)
reversed_num = int(str(num_abs)[::-1])
if is_negative:
    reversed_num = -reversed_num
print(f"The reversed number is: {reversed_num}")
