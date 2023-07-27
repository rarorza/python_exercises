# Develop a program where the user types any expression that uses parentheses.
# Your application should analyze whether the passed expression has the open
# and closed parentheses in the correct order.

expression = input("Type a expression: ").strip()
case_list = []
for case in expression:
    if case == "(":
        case_list.append(case)
    elif case == ")":
        if len(case_list) > 0:
            case_list.pop()
        else:
            case_list.append(case)
            break
if len(case_list) == 0:
    print("Your expression is valid!")
else:
    print("Your expression is wrong!")
