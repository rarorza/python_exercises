# Develop a program to read a phrase and show:
# 1 - How many times the "A" letter appears
# 2 - Where is the first position that appears
# 3 - Where is the last position that appears

phrase = input("Type a phrase: ").strip().upper()


print(
f"""The "A" letter appear {phrase.count("A")} times in the phrase
The first "A" letter appear in the position {phrase.find("A") + 1}
The last "A" letter appear in the position {phrase.rfind("A") + 1}"""
)
