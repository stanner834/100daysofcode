import random
import string
length = int(input("Enter a password length you would like?"))
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example: Generate a random password of length 12
password = generate_random_password(length)
print("Random Password:", password)
