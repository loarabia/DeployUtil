import urllib.request
import ssl
import http.cookiejar

#TODO: give an indicator of success
#TODO: handle errors a bit better.

class WDPRedirectHandler(urllib.request.HTTPRedirectHandler):

	def http_error_500(self, req, fp, code, msg, hdrs):
		self.http_error_307(req,fp,code,msg,hdrs)

	def http_error_307(self, req, fp, code, msg, hdrs):
		print("ERROR3")
		print(req)
		print(fp)
		print(code)
		print(msg)
		print(hdrs)

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
	print(cookies)
	print(cookies.cookiejar)
	opener = urllib.request.build_opener(WDPRedirectHandler(), https_handler, cookies)
	resp = opener.open(request)
	print(cookies)
	print(cookies.cookiejar)
	cookies.cookiejar.save(ignore_discard=True)

