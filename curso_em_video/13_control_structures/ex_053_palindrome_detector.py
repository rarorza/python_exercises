# Develop a program that reads any sentence and says if it is a palindrome,
# disregarding the spaces.

phrase = input("Digite uma frase: ").replace(" ", "").lower()
reverse_phrase = ""

for letter in range(len(phrase) - 1, -1, -1):
    reverse_phrase += phrase[letter]
# This for will reverse what was typed in the input:
# 1) len(phrase) - 1 = is the beginning of the range, that is, it starts from
# the end
# 2) -1 = this is the end of the range, going to 0, if we put 0 it will only go
# to 1, that's why the -1
# 3) -1 = is the range step, always subtracting 1

print(f"The inverse of {phrase} is {reverse_phrase}")

if phrase == reverse_phrase:
    print("We have a palindrome!")
else:
    print("The sentence entered is not a palindrome!")
