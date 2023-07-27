# Do a program to read some input and show the primitive type and all
# information possible about it.

everything = input("Type something: ")

print("The primitive type of that value is ", type(everything))
print("Is it a number? ", everything.isnumeric())
print("Is it a alphabet? ", everything.isalpha())
print("Is it a alphanumeric? ", everything.isalnum())
print("Is it in capitalize? ", everything.isupper())
print("Is it in lower case? ", everything.islower())
print("Is it start with a upper case letter? ", everything.istitle())
