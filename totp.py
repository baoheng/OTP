import pyotp

def generate_totp(key):
	totp = pyotp.TOTP(key)
	return totp.now()

def generate_key():
	return pyotp.random_base32()