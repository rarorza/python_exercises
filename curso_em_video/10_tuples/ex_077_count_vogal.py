# Develop a program that has a tuple with several words. After that, you must
# show, for each word, which are its vowels.
words = (
    "learn",
    "program",
    "language",
    "course",
    "video",
    "free",
    "study",
    "work",
    "practice",
    "future",
    "developer",
)

vowels = ["a", "e", "i", "o", "u"]

for word in words:
    print(f"In the word {word.upper()} we have ", end="")
    for letter in word:
        for vowel in vowels:
            if letter == vowel:
                print(f"{letter.upper()}", end=" ")
    print("")
