# Develop a program that reads the first term and ratio of an AP. At the end,
# show the first 10 terms of this progression.

print("=" * 25)
print("10 terms of a AP".center(25))
print("=" * 25)
init_term = int(input("First term: "))
ratio = int(input("Ratio: "))
final_term = init_term - ratio
# The final term is equal to the initial term minus the ratio,
# to the counter does not skip the initial term.

for i in range(1, 11):
    final_term += ratio
    print(f"{final_term}", end=" -> ")
print("END")
