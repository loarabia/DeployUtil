import urllib.request
import ssl

def create_toolsess_httpsHandler():
	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	context.verify_mode = ssl.CERT_NONE
	https_handler = urllib.request.HTTPSHandler(context=context)
	return https_handler
