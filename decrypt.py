import sys
from cryptography.fernet import Fernet

def decrypt_file(file_path, destination, key):
    with open(file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data)

    with open(destination, 'wb') as dec_file:
        dec_file.write(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python decrypt.py <file_path> <target_file_path> <key>")
        sys.exit(1)

    file_path = sys.argv[1]
    destination = sys.argv[2]
    key = sys.argv[3]
    
    decrypt_file(file_path, destination, key.encode())
