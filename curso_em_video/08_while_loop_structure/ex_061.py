# Redo CHALLENGE 051, reading the first term and the ratio of an AP, showing the
# first 10 terms of the progression using the while structure.

print("=" * 25)
print("10 TERMS OF A PA".center(25))
print("=" * 25)
first_term = int(input("First term: "))
reason = int(input("Reason: "))
final_term = first_term + (10 * reason)

while first_term < final_term:
    print(f"{first_term}", end=" -> ")
    first_term += reason
print("END")
