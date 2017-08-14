# storing keys for each client in a text file
# BAD practice, in real life use proper secure database

fileName = 'key-files.txt'
totpFile = 'totp-code'
def store_key(clientName='', origin='', key=''):
	f = open(fileName, 'r+')
	oldLines = f.readlines()
	f.close()
	f = open(fileName, 'w+')
	dataToFind = clientName + ':' + origin
	replaceOldLine = False
	strToWrite = ''
	for l in oldLines:
		if dataToFind in l:
			oldKey = l.split(':')[2]
			l = l.replace(oldKey, key) + '\n'
			replaceOldLine = True
		strToWrite += l
	if not replaceOldLine:
		strToWrite += clientName + ':' + origin + ':' + key + '\n'
	f.write(strToWrite)
	f.close()

def retrieve_key(clientName='', origin=''):
	lines = None
	with open(fileName, 'r') as f:
		lines = f.readlines()
		f.close()

	dataToFind = clientName + ':' + origin
	for l in lines:
		if dataToFind in l:
			return l.split(':')[2].replace('\n', '')
	return None

def store_totp_code(clientName='', origin='', totpCode=''):
	f = open(totpFile, 'r+')
	oldLines = f.readlines()
	f.close()
	f = open(totpFile, 'w+')
	dataToFind = clientName + ':' + origin
	replaceOldLine = False
	strToWrite = ''
	for l in oldLines:
		if dataToFind in l:
			oldTotpCode = l.split(':')[2]
			l = l.replace(oldTotpCode, totpCode) + '\n'
			replaceOldLine = True
		strToWrite += l
	if not replaceOldLine:
		strToWrite += clientName + ':' + origin + ':' + totpCode + '\n'
	f.write(strToWrite)
	f.close()

def verify_totp_code(clientName='', origin='', totpCode=''):
	lines = None
	with open(totpFile, 'r+') as f:
		lines = f.readlines()
		f.close()

	dataToFind = clientName + ':' + origin + ':' + totpCode
	for l in lines:
		if dataToFind in l:
			return True
	return False