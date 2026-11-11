def print_board(board):
    """Выводит текущее игровое поле в консоль."""
    print("---------")
    for row in board:
        print("| " + " ".join(row) + " |")
    print("---------")


def check_winner(board, symbol):
    """Проверяет, есть ли три одинаковых символа в ряд/столбец/диагональ."""

    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True


    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Проверяет, заполнена ли сетка."""
    for row in board:
        if " " in row or "_" in row:
            return False
    return True


def main():

    board = [[" " for _ in range(3)] for _ in range(3)]


    print_board(board)

    current_player = "X"

    while True:
        user_input = input("Enter the coordinates: ").strip().split()


        if len(user_input) != 2 or not all(part.isdigit() for part in user_input):
            print("You should enter numbers!")
            continue

        col, row = int(user_input[0]), int(user_input[1])


        if not (1 <= col <= 3 and 1 <= row <= 3):
            print("Coordinates should be from 1 to 3!")
            continue



        r_idx = row - 1
        c_idx = col - 1


        if board[r_idx][c_idx] != " " and board[r_idx][c_idx] != "_":
            print("This cell is occupied! Choose another one!")
            continue


        board[r_idx][c_idx] = current_player
        print_board(board)


        if check_winner(board, current_player):
            print(f"{current_player} wins")
            break
        elif is_board_full(board):
            print("Draw")
            break


        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()