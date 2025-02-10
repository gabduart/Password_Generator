import string
import random
import hashlib
import json
from datetime import datetime
from tabulate import tabulate
import os

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(password, filename='passwords.json'):
    encrypted_password = encrypt_password(password)
    creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []

    password_id = len(data) + 1
    password_data = {
        'id': password_id,
        'password': encrypted_password,
        'creation_date': creation_date
    }

    data.append(password_data)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def get_all_passwords(filename='passwords.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

if __name__ == "__main__":
    while True:
        print("Menu:")
        print("[1] Generate password")
        print("[2] Get all passwords")
        print("[3] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            os.system("cls")
            new_password = generate_password()
            save_password(new_password)
            print("Password generated and saved successfully.")
        elif choice == '2':
            os.system("cls")
            all_passwords = get_all_passwords()
            print("All passwords:")
            print(tabulate(all_passwords, headers="keys", tablefmt="grid"))
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")