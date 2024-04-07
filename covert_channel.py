import os
import tempfile
from cryptography.fernet import Fernet

# Function to generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data using AES
def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Function to decrypt data using AES
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

# Function to write data to a file securely and with encryption
def secure_write_to_file(file_path, data, key):
    encrypted_data = encrypt_data(data, key)
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(encrypted_data)
            temp_file_path = temp_file.name
        os.rename(temp_file_path, file_path)
        print(f"Secure and encrypted data written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to read data from a file securely and with decryption
def secure_read_from_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = decrypt_data(encrypted_data, key)
        print(f"Secure and decrypted data read from {file_path}: {decrypted_data}")
        return decrypted_data
    except Exception as e:
        print(f"Error reading from file: {e}")

# Using the functions to write and read securely with encryption
if __name__ == "__main__":
    key = generate_key() # Generate a key for encryption
    # Writing data to a file securely and with encryption
    secure_write_to_file('secure_secret_channel.txt', 'Hello, this is a secure secret message.', key)

    # Reading data from a file securely and with decryption
    secure_read_from_file('secure_secret_channel.txt', key)
