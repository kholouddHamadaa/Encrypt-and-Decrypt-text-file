from cryptography.fernet import Fernet

# load the same key
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('enc_job.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_job.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

print("File decrypted successfully")
