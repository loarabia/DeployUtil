import urllib.request
import ssl
import http.cookiejar

#TODO: give an indicator of success
#TODO: handle errors a bit better.

def do_pair(ip, pin, **_args):
	# IF YOU DON'T DO THIS OVER HTTPS YOU WILL GET 308s to goto HTTPS
	scheme = 'https://'
	port = ''
	api = '/api/authorize/pair?pin={pin}&persistent=0'
	verb = 'POST'

	request_url = scheme + ip + port + api.format_map({'pin':pin})

	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	context.verify_mode = ssl.CERT_NONE
	https_handler = urllib.request.HTTPSHandler(context=context)

	request = urllib.request.Request(url=request_url, method=verb)

	cookies = urllib.request.HTTPCookieProcessor(http.cookiejar.MozillaCookieJar("deployUtil.cookies"))
	opener = urllib.request.build_opener(WDPRedirectHandler(), https_handler, cookies)
	resp = opener.open(request)
	cookies.cookiejar.save(ignore_discard=True)
