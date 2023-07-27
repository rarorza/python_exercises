# Develop a program to read a name of city and display it if the name start
# with "Santo".

city = str(input("What city were you born in? ")).strip().lower()
split_city = city.split()
verify_city = split_city[0].find("santo")

if verify_city == -1:
    print("False")
else:
    print("True")
