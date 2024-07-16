# Encrypted .env Management

This repository provides tools to securely manage `.env` files by encrypting and decrypting them using the `cryptography` library. The `.env` file contains sensitive information like API keys, and these tools help keep it secure.

## Files

- `env_encryptor.py`: Encrypts the `.env` file.
- `env_decryptor.py`: Decrypts the `.env` file and restores it to its original state.
- `env_utils.py`: Provides utility functions for decrypting, loading, and re-encrypting the `.env` file, and accessing its variables securely.

## Setup

1. **Install dependencies:**
   ```bash
   pip install cryptography python-dotenv
   ```

2. **Generate a key:**
   Ensure you have a `secret.key` file generated. This is needed for encryption and decryption.

   ```python
   from cryptography.fernet import Fernet

   key = Fernet.generate_key()
   with open("secret.key", "wb") as key_file:
       key_file.write(key)
   ```

## Usage

### Encrypting the `.env` File

Use the `env_encryptor.py` script to encrypt your `.env` file.

```bash
python env_encryptor.py
```

### Decrypting the `.env` File

Use the `env_decryptor.py` script to decrypt your `.env` file and save it back to its original state.

```bash
python env_decryptor.py
```

### Accessing Environment Variables Securely

Use the `env_utils.py` module in your scripts to access environment variables securely.

Example:

```python
from env_utils import get_env_variable

if __name__ == "__main__":
    api_key = get_env_variable("API_KEY")
    print(f"API_KEY: {api_key}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
