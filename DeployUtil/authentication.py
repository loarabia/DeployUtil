import requests
import json

#TODO: give an indicator of success
#TODO: handle errors a bit better.
#TODO: I think I can simplify the API string and pass key value pairs
#	as a dict to the requests module and it will handle turning
#	those into query strings for me

def do_pair(ip, pin, **_args):
	# IF YOU DON'T DO THIS OVER HTTPS YOU WILL GET 308s to goto HTTPS
	# But we cannot verify our HTTPS cert yet because we cannot get it off
	# of all devices.
	# If the tooling gets smarter about what its talking to, then we can
	# make an educated choice.
	scheme = 'https://'
	port = ''
	api = '/api/authorize/pair?pin={pin}&persistent=0'
	request_url = scheme + ip + port + api.format_map({'pin':pin})

	with requests.Session() as session:
		response = session.post(request_url, verify=False)
		cookie_filename = 'deployUtil.cookies'
		cookies = requests.utils.dict_from_cookiejar(response.cookies)
		with open(cookie_filename,'w') as cookie_file:
			json.dump(cookies, cookie_file)
