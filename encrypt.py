from cryptography.fernet import Fernet

# generate key
key = Fernet.generate_key()

# save key
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

# load key
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('job_details.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_job.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

print("File encrypted successfully")
