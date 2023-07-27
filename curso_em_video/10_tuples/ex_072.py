# Develop a program which has a fully populated tuple with a count spelled out
# from zero to twenty.
# Your program should read the input (between 0 and 20) and display it in words.

num_in_words = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
)

num = int(input("Type a number(between 0 and 20): "))
while True:
    if 0 <= num <= 20:
        print(f"You typed the number {num_in_words[num]}")
        break
    else:
        num = int(input("Try again. Type a number between 0 and 20: "))
