import string
import random
import hashlib
import json
from datetime import datetime

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(password, filename='passwords.json'):
    encrypted_password = encrypt_password(password)
    creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    password_data = {
        'password': encrypted_password,
        'creation_date': creation_date
    }
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(password_data)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    new_password = generate_password()
    save_password(new_password)
    print("Password generated and saved successfully.")