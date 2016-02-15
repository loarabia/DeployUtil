import urllib.request
import http.cookiejar
import DeployUtil.toolsession as session
import json

def do_list(ip, pretty, **_args):
	scheme = 'https://'
	port = ''
	api = '/api/app/packagemanager/packages?'
	verb = 'GET'

	request_url = scheme + ip + port + api
	request = urllib.request.Request(url=request_url, method=verb)

	https_handler = session.create_toolsess_httpsHandler()

	cookies = urllib.request.HTTPCookieProcessor(http.cookiejar.MozillaCookieJar("deployUtil.cookies"))
	cookies.cookiejar.load(ignore_discard=True)
	opener = urllib.request.build_opener(https_handler, cookies)
	resp = opener.open(request)

	json_obj = json.loads(resp.read().decode())
	return json_obj
