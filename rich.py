# Creadted by Linzuyao
# This is the main file of rich project
from get_commands import Command

if __name__ == "__main__":
    later_to_decide = Command()

while True:
    command = later_to_decide.get_user_input()
    if command == "quit":
        break
    elif command == "roll":
        pass
    elif command == "sell":
        pass
    elif command == "block":
        pass
    elif command == "robot":
        pass
    elif command == "help":
        pass
    elif command == "query":
        pass
    elif command == "step":
        pass
    else:
        print("Your input a bad command,please repeat.")
