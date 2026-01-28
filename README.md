🔐 File Encryption & Decryption using Python (Fernet)
📌 Description

This project demonstrates how to securely encrypt and decrypt files using Python’s cryptography library with the Fernet symmetric encryption algorithm.
It ensures data confidentiality by using the same secret key for both encryption and decryption.

🛠️ Technologies Used

Python 3

cryptography (Fernet)

📂 Project Structure
encryption-project/
│
├── main.py          # Encrypts the CSV file
├── decrypt.py       # Decrypts the encrypted file
├── mykey.key        # Secret encryption key
├── job_details.csv  # Original file
├── enc_job.csv      # Encrypted file
└── dec_job.csv      # Decrypted file

🔑 How It Works

A secret key is generated using Fernet.

The key is saved to a file (mykey.key).

The original CSV file is encrypted using the key.

The encrypted file can only be decrypted using the same key.

▶️ How to Run
1️⃣ Install dependencies
pip install cryptography

2️⃣ Encrypt the file
python main.py


This will generate:

mykey.key

enc_job.csv

3️⃣ Decrypt the file
python decrypt.py


This will generate:

dec_job.csv

⚠️ Important Notes

The same key must be used for encryption and decryption.

Generating a new key during decryption will result in:

cryptography.fernet.InvalidToken


Keep mykey.key secure. Losing it means the data cannot be decrypted.

👩‍💻 Author

Kholoud Hamada
Python Learner & Aspiring Data Engineer