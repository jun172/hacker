from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

encrypted = cipher.encrypt(b"secret data")
decrypted = cipher.decrypt(encrypted)

print(decrypted)