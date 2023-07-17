# Improve CHALLENGE 061, asking the user if he wants to show some more terms.
# The program exits when the user says he wants to show 0 terms.

def main():
    print("=" * 25)
    print("PA GENERATOR".center(25))
    print("=" * 25)
    first_term = int(input("First term: "))
    reason = int(input("Reason: "))
    terms = 10
    count_terms = terms
    final_term = first_term + (terms * reason)
    progression(first_term, final_term, reason)
    option = 1
    while option != 0:
        option = int(input("How many terms do you want to show more? "))
        terms = option
        count_terms += option
        first_term = final_term
        final_term = first_term + (terms * reason)
        progression(first_term, final_term, reason)
    print(f"Progression finished with {count_terms} shown")


def progression(first_term, final_term, reason):
    while first_term < final_term:
        print(f"{first_term}", end=" -> ")
        first_term += reason
    print("PAUSE")


if __name__ == "__main__":
    main()
