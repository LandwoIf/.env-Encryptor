from cryptography.fernet import Fernet
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

if __name__ == "__main__":
    # Specify the file name to be decrypted here
    file_to_decrypt = ".env"
    
    decrypt_file(file_to_decrypt)
