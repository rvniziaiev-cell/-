import random


def get_initial_pencils():
    """Запрашивает и валидирует начальное количество карандашей."""
    while True:
        user_input = input("How many pencils would you like to use:\n> ").strip()

        # Проверка 1: Строка должна состоять только из цифр
        if not user_input.isdigit():
            print("The number of pencils should be numeric")
            continue

        pencils = int(user_input)

        # Проверка 2: Количество должно быть больше 0
        if pencils == 0:
            print("The number of pencils should be positive")
            continue

        return pencils


def get_first_player(player1, player2):
    """Запрашивает и валидирует выбор первого игрока."""
    while True:
        choice = input(f"Who will be the first ({player1}, {player2}):\n> ").strip()
        if choice in (player1, player2):
            return choice
        print(f"Choose between '{player1}' and '{player2}'")


def get_bot_move(pencils):
    """Вычисляет ход бота לפי выигрышной стратегии."""
    # Выигрышные позиции оставляют сопернику (4n + 1) карандашей
    remainder = pencils % 4

    if remainder == 0:
        return 3
    elif remainder == 3:
        return 2
    elif remainder == 2:
        return 1
    else:  # Проигрышная позиция (pencils % 4 == 1)
        if pencils == 1:
            return 1
        return random.randint(1, min(3, pencils))


def get_human_move(pencils):
    """Запрашивает и валидирует ход человека-игрока."""
    while True:
        user_input = input("> ").strip()

        # Проверка 1: Допустимые значения только 1, 2, 3
        if user_input not in ('1', '2', '3'):
            print("Possible values: '1', '2' or '3'")
            continue

        take = int(user_input)

        # Проверка 2: Нельзя взять больше карандашей, чем осталось
        if take > pencils:
            print("Too many pencils were taken")
            continue

        return take


def main():
    player_human = "John"
    player_bot = "Jack"

    pencils = get_initial_pencils()
    current_player = get_first_player(player_human, player_bot)

    while pencils > 0:
        # Выводим текущее количество карандашей вертикальными линиями '|'
        print("|" * pencils)

        if current_player == player_human:
            print(f"{current_player}'s turn!")
            take = get_human_move(pencils)
        else:
            print(f"{current_player}'s turn:")
            take = get_bot_move(pencils)
            print(take)  # Печатаем выбранный ботом ход

        pencils -= take

        # Передаем ход следующему игроку
        current_player = player_bot if current_player == player_human else player_human

    # Победитель — тот, ЧИЙ сейчас ход (так как предыдущий взял последний карандаш и проиграл)
    winner = current_player
    print(f"{winner} won!")


if __name__ == "__main__":
    main()