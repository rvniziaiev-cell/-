def read_matrix(prompt=""):
    """Считывает размеры и элементы матрицы от пользователя."""
    if prompt:
        print(prompt)
    size_str = input("Enter matrix size: > ").strip().split()
    n, m = int(size_str[0]), int(size_str[1])
    print("Enter matrix:")
    matrix = []
    for _ in range(n):
        row = [float(x) for x in input("> ").strip().split()]
        matrix.append(row)
    return matrix, n, m


def print_matrix(matrix):
    """Выводит матрицу в консоль."""
    print("The result is:")
    for row in matrix:
        formatted_row = []
        for val in row:
            # Округление до 2-4 знаков для красивого вывода или отображение целых чисел
            if isinstance(val, float) and val.is_integer():
                formatted_row.append(str(int(val)))
            elif isinstance(val, float):
                formatted_row.append(f"{round(val, 4):g}")
            else:
                formatted_row.append(str(val))
        print(" ".join(formatted_row))


# 1. Сложение матриц
def add_matrices():
    size1 = input("Enter size of first matrix: > ").strip().split()
    n1, m1 = int(size1[0]), int(size1[1])
    print("Enter first matrix:")
    m1_data = [[float(x) for x in input("> ").strip().split()] for _ in range(n1)]

    size2 = input("Enter size of second matrix: > ").strip().split()
    n2, m2 = int(size2[0]), int(size2[1])
    print("Enter second matrix:")
    m2_data = [[float(x) for x in input("> ").strip().split()] for _ in range(n2)]

    if n1 != n2 or m1 != m2:
        print("The operation cannot be performed.")
        return

    result = [[m1_data[i][j] + m2_data[i][j] for j in range(m1)] for i in range(n1)]
    print_matrix(result)


# 2. Умножение на константу
def multiply_by_constant():
    matrix, n, m = read_matrix()
    const = float(input("Enter constant: > ").strip())
    result = [[matrix[i][j] * const for j in range(m)] for i in range(n)]
    print_matrix(result)


# 3. Умножение матриц
def multiply_matrices():
    size1 = input("Enter size of first matrix: > ").strip().split()
    n1, m1 = int(size1[0]), int(size1[1])
    print("Enter first matrix:")
    m1_data = [[float(x) for x in input("> ").strip().split()] for _ in range(n1)]

    size2 = input("Enter size of second matrix: > ").strip().split()
    n2, m2 = int(size2[0]), int(size2[1])
    print("Enter second matrix:")
    m2_data = [[float(x) for x in input("> ").strip().split()] for _ in range(n2)]

    if m1 != n2:
        print("The operation cannot be performed.")
        return

    result = [[sum(m1_data[i][k] * m2_data[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]
    print_matrix(result)


# 4. Транспонирование
def transpose_main(m, rows, cols):
    return [[m[j][i] for j in range(rows)] for i in range(cols)]


def transpose_side(m, rows, cols):
    return [[m[rows - 1 - j][cols - 1 - i] for j in range(rows)] for i in range(cols)]


def transpose_vertical(m, rows, cols):
    return [[m[i][cols - 1 - j] for j in range(cols)] for i in range(rows)]


def transpose_horizontal(m, rows, cols):
    return [[m[rows - 1 - i][j] for j in range(cols)] for i in range(rows)]


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: > ").strip()
    matrix, n, m = read_matrix()

    if choice == "1":
        print_matrix(transpose_main(matrix, n, m))
    elif choice == "2":
        print_matrix(transpose_side(matrix, n, m))
    elif choice == "3":
        print_matrix(transpose_vertical(matrix, n, m))
    elif choice == "4":
        print_matrix(transpose_horizontal(matrix, n, m))


# 5. Детерминант
def get_submatrix(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        sub = get_submatrix(matrix, 0, j)
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def calculate_determinant():
    matrix, n, m = read_matrix()
    if n != m:
        print("The operation cannot be performed.")
        return
    det = determinant(matrix)
    print("The result is:")
    if isinstance(det, float) and det.is_integer():
        print(int(det))
    else:
        print(f"{round(det, 4):g}")


# 6. Обратная матрица
def inverse_matrix():
    matrix, n, m = read_matrix()
    if n != m:
        print("This matrix doesn't have an inverse.")
        return

    det = determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    if n == 1:
        print_matrix([[1 / det]])
        return

    # Вычисление матрицы алгебраических дополнений (cofactors)
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            sub = get_submatrix(matrix, i, j)
            cofactor_row.append(((-1) ** (i + j)) * determinant(sub))
        cofactors.append(cofactor_row)

    # Транспонирование матрицы сомножителей (союзная матрица)
    adjugate = transpose_main(cofactors, n, n)

    # Деление союзной матрицы на детерминант
    inverse = [[adjugate[i][j] / det for j in range(n)] for i in range(n)]
    print_matrix(inverse)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: > ").strip()

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()