# Count the number of spaces in a string

from faker import Faker

faker = Faker("pt_BR")

random_string = faker.text(200)

result = len([space for space in random_string if " " in str(space)])

print(result)