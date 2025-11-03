print("Om Nimmalwar")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
mat1 = [[int(input()) for _ in range(cols)] for _ in range(rows)]

print("Enter elements of second matrix:")
mat2 = [[int(input()) for _ in range(cols)] for _ in range(rows)]

result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]

print("Resultant Matrix:")
for r in result:
    print(r)
