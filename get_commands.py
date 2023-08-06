# Created by Linzuyao
# The module has the functions and the classes and so on to get user commands
from colorama import Fore


class Command:
    def __init__(self, role=None) -> None:
        self.role = role

    def get_user_input(self) -> str:
        choose_role_color = {
            "Q": Fore.GREEN,
            None: Fore.WHITE,
            "A": Fore.RED,
            "J": Fore.BLUE,
        }
        command = input(choose_role_color[self.role] + "$ ").strip().lower()
        print(Fore.RESET, end="")
        return command


if __name__ == "__main__":
    test = Command("A")
    print(test.get_user_input())
