# ENV Encryptor

from cryptography.fernet import Fernet
import os

# Generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from the current directory named `secret.key`
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_name, "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    # Specify the file name to be encrypted here
    file_to_encrypt = ".env"
    
    # Check if the key file exists, if not generate a new one
    if not os.path.exists("secret.key"):
        generate_key()
        print("Generated new secret.key")

    encrypt_file(file_to_encrypt)
    print(f"{file_to_encrypt} has been encrypted.")
