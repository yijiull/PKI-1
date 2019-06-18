import hashlib, binascii, os
from cryptography.fernet import Fernet

def cryptoEmail():
    key = Fernet.generate_key()