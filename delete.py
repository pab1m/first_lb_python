columns = int(input("Введіть кількість стовпців: "))
rows = int(input("Введіть кількість рядків: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        el = int(input(f"Enter elements [{i}][{j}]: "))
        row.append(el)
    matrix.append(row)

digit = int(input("Enter a number for multiply matrix: "))

result_matrix = [[el * digit for el in row] for row in matrix]

for row in result_matrix:
    print(row)

