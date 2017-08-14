from flask import Flask, request, Response
import config, totp, mockdatabase

app = Flask(__name__)
app.config.from_object(config)

@app.route('/create_relation')
def create_relation():
	return 'Creating connection, please call generate_key to get the shared secret key', 200

@app.route('/generate_key')
def get_secret_key():
	clientName = request.headers.get('client-name')
	origin = request.headers.get('origin')
	key = totp.generate_key()
	mockdatabase.store_key(clientName, origin, key)
 	return key, 200

@app.route('/send_totp')
def send_totp():
	clientName = request.headers.get('client-name')
	origin = request.headers.get('origin')
	key = mockdatabase.retrieve_key(clientName, origin)
	if key is not None:
		totpCode = totp.generate_totp(key)
		mockdatabase.store_totp_code(clientName, origin, totpCode)
		return totpCode, 200
	return 'None Key exist for ' + clientName, 400

@app.route('/verify')
def verify():
	clientName = request.headers.get('client-name')
	origin = request.headers.get('origin')
	totpCode = request.headers.get('totp')
	hasCode = mockdatabase.verify_totp_code(clientName, origin, totpCode)
	if hasCode:
		return 'Verified!', 200
	else:
		return 'Not Verified!', 400

if __name__ == '__main__':
    app.run(debug=config.DEBUG)