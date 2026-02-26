from cryptography.fernet import Fernet
with open("secret.key", "rb") as key_file:
    key = key_file.read()
cipher = Fernet(key)
msg = "My password is Popcorn123!".encode()
enc = cipher.encrypt(msg)
with open("vault.encrypted", "wb") as f:
    f.write(enc)
print("Vault encrypted!")