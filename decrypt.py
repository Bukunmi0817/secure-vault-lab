from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

with open("vault.encrypted", "rb") as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)
print("Unlocked Message:", decrypted_data.decode())