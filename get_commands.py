# Created by Linzuyao
# The module has the functions and the classes and so on to get user commands
from colorama import Fore


class Command:
    def __init__(self, role=None) -> None:
        self.role = role

    def get_user_input(self) -> str:
        if self.role == "Q":
            command = input(Fore.GREEN + ">>>>>").strip().lower()
        elif self.role == "A":
            command = input(Fore.RED + ">>>>>").strip().lower()
        elif self.role == "J":
            command = input(Fore.BLUE + ">>>>>").strip().lower()
        else:
            command = input(">>>>>").strip().lower()
        print(Fore.RESET, end="")
        return command


if __name__ == "__main__":
    test = Command()
    print(test.get_user_input())
