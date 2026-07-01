# CLI Password Manager

A command-line tool that securely stores and retrieves login credentials using real encryption. 

## Features

- AES-128 Fernet symmetric encryption on every stored password
- Master key stored locally and never committed to the repository
- Add, retrieve, list, and delete credentials from the command line
- Passwords never visible on screen while typing 
- 7 tests covering functionality and error cases

## Tech Stack

Python 3.14, cryptography (Fernet/AES-128-CBC + HMAC), argparse, pytest, JSON

## Getting Started

```bash
git clone https://github.com/arzoo210/CLI-PASSWORD-MANAGER
cd cli-password-manager
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
python crypto_utils.py       
```

## Usage / Demo

```bash
# Add a credential
python password_manager.py add gmail arzoo123

# Retrieve a credential
python password_manager.py get gmail

# List all saved services
python password_manager.py list

# Delete a credential
python password_manager.py delete gmail
```

![Demo](assets/demo.gif)

## Security Model

Passwords are encrypted individually using Fernet symmetric encryption (AES-128-CBC + HMAC). The master key lives in `key.key` on your local machine and is never committed to the repo — without it, the encrypted data in `credentials.json` is completely unreadable. Usernames are stored as plaintext since they are not considered secret.


## Running Tests

```bash
pytest test_password_manager.py -v
```

## What I Learned

- How symmetric encryption works in practice using Fernet (AES + HMAC), and why you separate key generation from the main program logic
- How to build a real CLI with subcommands using Python's argparse module
- How to structure a project with separation of concerns (encryption, storage, and CLI logic in separate files) and write unit tests with pytest

## File Structure

```
cli-password-manager/
├── password_manager.py       # CLI entry point (argparse commands)
├── crypto_utils.py           # Encryption/decryption logic (Fernet)
├── storage.py                # JSON storage layer
├── test_passwordmanager.py  # pytest test (7 tests)
├── requirements.txt          # Project dependencies
├── .gitignore                # Excludes key.key, credentials.json, venv
└── README.md                 # This file
```