# Develop a mini-system that uses Python's interactive help. The user will type
# the command and the manual will appear. When the user types "END", the program
# will exit.


def pyHelper():
    while True:
        print("~" * 30)
        print("HELP SYSTEM PyHelper".center(30))
        print("~" * 30)
        print("function or library > ", end="")
        command = input()
        if command.upper().strip() == "END":
            print("~" * 30)
            print("See you later!".center(15))
            print("~" * 30)
            break
        else:
            print(f"Accessing the {command} command manual")
            help(command)


pyHelper()
