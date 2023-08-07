# Develop a program that has a grades() function that can receive several grades
# from students and will return a dictionary with the following information:
#
# - Number of notes
# - the highest grade
# - The lowest grade
# - The average of the class
# - The situation (optional)
# Also add the docstring.


def grades(*n, situation=False):
    """Function to analyze grades and situation of several students

    Keyword arguments:
    n -- one or more student grades (accepts multiple)
    situation -- optional value, indicating whether or not to add the status of
    the class
    Return: dictionary with various information about the situation of the class
    """
    class_dic = {
        "total": len(n),
        "biggest": max(n),
        "smallest": min(n),
        "average": sum(n) / len(n),
    }
    if situation:
        if class_dic.get("average") >= 7:
            class_dic["situation"] = "GOOD"
        if 5 <= class_dic.get("average") < 7:
            class_dic["situation"] = "MORE OR LESS"
        if class_dic.get("average") < 5:
            class_dic["situation"] = "BAD"

    return class_dic


class_situation = grades(5, 6, 6, situation=True)
print(class_situation)
help(grades)
