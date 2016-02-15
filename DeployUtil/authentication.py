import urllib.request

def do_pair(ip, pin, **_args):
	print(ip)
	print(pin)
	scheme = 'http://'
	#port = ':10080'
	port = ''
	api = '/api/app/authorize/pair?pin={pin}'
	verb = 'GET'

	request_url = scheme + ip + port + api.format_map({'pin':pin})
	request = urllib.request.Request(url=request_url, method=verb)
	try:
		response = urllib.request.urlopen(request)
	except urllib.error.HTTPError as err:
		print(err)

		
def do_list():
	pass
