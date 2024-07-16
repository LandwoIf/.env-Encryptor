from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

# Load the key from the current directory named `secret.key`
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        print("Key loaded successfully.")
        return key
    except FileNotFoundError:
        print("Error: secret.key file not found.")
        raise

# Decrypt the file
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_name, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_name, "wb") as file:
            file.write(decrypted_data)
        print(f"{file_name} decrypted successfully.")
    except Exception as e:
        print(f"Error decrypting {file_name}: {e}")
        raise

# Encrypt the file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)
    
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)

        with open(file_name, "wb") as file:
            file.write(encrypted_data)
        print(f"{file_name} encrypted successfully.")
    except Exception as e:
        print(f"Error encrypting {file_name}: {e}")
        raise

# Utility function to load .env variables securely
def load_encrypted_env(file_name=".env"):
    # Decrypt the .env file
    decrypt_file(file_name)
    
    # Load the .env file
    load_dotenv(file_name)
    print(".env file loaded successfully.")
    
    # Optionally, re-encrypt the .env file
    encrypt_file(file_name)

# Function to get environment variable securely
def get_env_variable(key, file_name=".env"):
    load_encrypted_env(file_name)
    value = os.getenv(key)
    encrypt_file(file_name)  # Re-encrypt the .env file after reading
    return value
