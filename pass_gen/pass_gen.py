import string
import random

length = int(input("Password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
