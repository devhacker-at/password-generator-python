import random
import string

# Ask user for password length
length = int(input("Enter password length: "))

# Characters to use in password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
