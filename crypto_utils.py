from cryptography.fernet import Fernet
KEY_FILE = "key.key"
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
        print("key generated and saved to {KEY_FILE}")

def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()
    
def get_fernet():
    key = load_key()
    return Fernet(key)

def encrypt(text: str) -> str:
    f = get_fernet()
    encrypted_bytes = f.encrypt(text.encode())
    return encrypted_bytes.decode()

def decrypt(token: str) -> str:
    f = get_fernet()
    decrypted_bytes = f.decrypt(token.encode())
    return decrypted_bytes.decode()

if __name__ == "__main__":
    generate_key()