class CoffeeMachine:
    def __init__(self):
        # Начальные запасы ресурсов и денег (Этапы 4-6)
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

        # Переменные состояния
        self.state = "CHOOSING_ACTION"
        self.fill_stage = 0
        self.running = True

        # Параметры напитков: [water, milk, beans, cost]
        self.recipes = {
            "1": [250, 0, 16, 4],  # Espresso
            "2": [350, 75, 20, 7],  # Latte
            "3": [200, 100, 12, 6]  # Cappuccino
        }

    def process_input(self, user_input):
        """Единый метод обработки входящих команд (Этап 6)."""
        user_input = user_input.strip()

        if self.state == "CHOOSING_ACTION":
            self._handle_action(user_input)
        elif self.state == "CHOOSING_COFFEE":
            self._handle_buy(user_input)
        elif self.state == "FILLING":
            self._handle_fill(user_input)

    def _handle_action(self, action):
        if action == "buy":
            self.state = "CHOOSING_COFFEE"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        elif action == "fill":
            self.state = "FILLING"
            self.fill_stage = 0
            print("Write how many ml of water do you want to add:")
        elif action == "take":
            print(f"I gave you {self.money}")
            self.money = 0
            self._prompt_action()
        elif action == "remaining":
            self.print_status()
            self._prompt_action()
        elif action == "exit":
            self.running = False

    def _handle_buy(self, choice):
        if choice == "back":
            self.state = "CHOOSING_ACTION"
            self._prompt_action()
            return

        if choice in self.recipes:
            w_req, m_req, b_req, cost = self.recipes[choice]

            # Проверка достаточности ресурсов
            if self.water < w_req:
                print("Sorry, not enough water!")
            elif self.milk < m_req:
                print("Sorry, not enough milk!")
            elif self.beans < b_req:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= w_req
                self.milk -= m_req
                self.beans -= b_req
                self.cups -= 1
                self.money += cost

        self.state = "CHOOSING_ACTION"
        self._prompt_action()

    def _handle_fill(self, user_input):
        try:
            amount = int(user_input)
        except ValueError:
            amount = 0

        if self.fill_stage == 0:
            self.water += amount
            self.fill_stage = 1
            print("Write how many ml of milk do you want to add:")
        elif self.fill_stage == 1:
            self.milk += amount
            self.fill_stage = 2
            print("Write how many grams of coffee beans do you want to add:")
        elif self.fill_stage == 2:
            self.beans += amount
            self.fill_stage = 3
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.fill_stage == 3:
            self.cups += amount
            self.state = "CHOOSING_ACTION"
            self._prompt_action()

    def print_status(self):
        """Выводит текущее состояние ресурсов кавомашины."""
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def _prompt_action(self):
        print("Write action (buy, fill, take, remaining, exit):")


def main():
    machine = CoffeeMachine()
    machine._prompt_action()

    while machine.running:
        user_input = input("> ")
        machine.process_input(user_input)


if __name__ == "__main__":
    main()