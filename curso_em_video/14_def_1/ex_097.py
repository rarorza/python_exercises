# Write a program that has a function called write(), which receives any text as
# a parameter and displays a message with an adaptable size.
# Ex: write("Hello World")
# Out:
# ~~~~~~~~~~~~~~
#  Hello World!
# ~~~~~~~~~~~~~~
def write(text):
    print("~" * (len(text) + 2))
    print(f"{text}".center(len(text) + 2))
    print("~" * (len(text) + 2))


while True:
    text = input("Type your message (exit to stop): ")
    if "exit" in text:
        break
    write(text)
