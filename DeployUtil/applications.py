import json
import requests

#TODO What happens if I don't have a cookie? There are a few possibilities.
#	1. Authentication is turned off and then probably I don't care
#	2. Authentication isn't cookie based. Need more logic
#	3. There is an error, so I really need to go back and tell the user get
#		a cookie if they can
#	4. There was some error in the session (network timeout, file read
#		failure, etc.) Let the user know and exit.
def do_list(ip, **_args):
	scheme = 'https://'
	port = ''
	api = '/api/app/packagemanager/packages?'
	request_url = scheme + ip + port + api

	with requests.Session() as session:
		cookie_filename = 'deployUtil.cookies'
		with open(cookie_filename,'r') as cookie_file:
			cookies = json.load(cookie_file)
			response = session.get(	request_url,
						verify=False,
						cookies=cookies)
			json_obj = json.loads(response.text)
			return json_obj

def do_install(ip, appx, deps, **_args):
	pass
