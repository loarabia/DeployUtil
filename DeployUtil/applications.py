import urllib.request
import ssl
import http.cookiejar

def do_list(ip, pretty, **_args):
	print(ip)
	print(pretty)
	scheme = 'https://'
	port = ''
	api = '/api/app/packagemanager/packages?'
	verb = 'GET'

	request_url = scheme + ip + port + api
	print(request_url)
	request = urllib.request.Request(url=request_url, method=verb)

	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	context.verify_mode = ssl.CERT_NONE
	https_handler = urllib.request.HTTPSHandler(context=context)

	cookies = urllib.request.HTTPCookieProcessor(http.cookiejar.MozillaCookieJar("deployUtil.cookies"))
	cookies.cookiejar.load(ignore_discard=True)
	print(cookies.cookiejar)
	opener = urllib.request.build_opener(https_handler, cookies)
	resp = opener.open(request)
	print(resp.read())
