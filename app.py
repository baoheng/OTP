from flask import Flask, request
import config, totp

app = Flask(__name__)
app.config.from_object(config)

@app.route('/generate_key')
def get_secret_key():
    return totp.generate_key()

@app.route('/send_totp')
def send_totp():
	key = request.args.get('secret')
	if key is None:
		return Response('No secret key passed in.', 404, 'text/plaine')
	return Response(totp.generate_totp(key), 200, 'text/plaine')


if __name__ == '__main__':
    app.run(debug=config.DEBUG)