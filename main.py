import string
import random
import hashlib

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if __name__ == "__main__":
    password = generate_password()
    print("Generated password:", password)
    print("Encrypted password:", encrypt_password(password))