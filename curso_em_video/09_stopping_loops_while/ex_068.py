# Develop a program that matches even or odd with the computer. The game will
# only be interrupted when the player LOSES, showing the total number of
# consecutive victories he has achieved at the end of the game.

from random import randint

print("=-" * 15)
print("LET'S PLAY ODD OR EVEN".center(30))
count = 0

while True:
    print("=-" * 15)
    num = int(input("Enter a value: "))
    option = " "
    while option not in "EeOo":
        option = input("Even or odd? [E/O]").strip().upper()[0]

    random_num = randint(0, 10)
    result = num + random_num
    print("-" * 30)

    if result % 2 == 0:
        print(
            f"""
You played {num} and the computer {random_num}, total of {result}. IT EVEN!
            """
        )
        if option in "Ee":
            print("You WIN!")
            count += 1
            print("Let's play again...")
        elif option in "Oo":
            print("You LOST!")
            print("=-" * 15)
            break
    else:
        print(
            f"""
You played {num} and the computer {random_num}, total of {result}. IT ODD!
              """
        )
        if option in "Oo":
            print("You WIN!")
            count += 1
            print("Let's play again...")
        elif option in "Ee":
            print("You LOST!")
            print("=-" * 15)
            break
print(f"GAME OVER! you won {count} times.")
