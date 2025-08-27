from cryptography.fernet import Fernet
import os
import json

SECRET_KEY_FILE = "secure/secret.key"
NOTES_FILE = "secure/notes.json"

# Generate and store key
def load_key():
    if not os.path.exists("secure"):
        os.makedirs("secure")
    if not os.path.exists(SECRET_KEY_FILE):
        key = Fernet.generate_key()
        with open(SECRET_KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(SECRET_KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_key()

# Save note securely
def save_secure_note(title, content):
    encrypted = fernet.encrypt(content.encode()).decode()
    notes = load_notes()
    notes[title] = encrypted
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

# Load and decrypt note
def load_secure_note(title):
    notes = load_notes()
    if title in notes:
        try:
            return fernet.decrypt(notes[title].encode()).decode()
        except:
            return None
    return None

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r") as f:
        return json.load(f)
