import pyotp, os

from cryptography.fernet import Fernet

def generate_totp(key):
	totp = pyotp.TOTP(os.urandom(16))
	return totp.now()

print pyotp.random_base32()