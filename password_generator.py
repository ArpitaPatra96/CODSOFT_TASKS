import random
import string

print("******** Password Generator ********")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    random_character = random.choice(characters)
    password = password + random_character

print("\nGenerated Password is:", password)

print("\nThank you!")