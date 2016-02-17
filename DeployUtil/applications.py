import json
import requests
import pathlib
import os.path
import base64

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

#TODO add state queries to determine if the command is done. Not sure yet if
#	here or in the commandline tool.
#TODO add the ability to search through the dependencies dir more thoroughly
#TODO add a good response
def do_install(ip, appx, depsdir, **_args):
	scheme = 'https://'
	port = ''
	api = '/api/app/packagemanager/package?'
	request_url = scheme + ip + port + api

	with requests.Session() as session:
		cookie_filename = 'deployUtil.cookies'
		with open(cookie_filename,'r') as cookie_file:
			cookies = json.load(cookie_file)

			files = []
			# Get the Appx
			full_appx_path = os.path.abspath(appx)
			appx_path = pathlib.Path(full_appx_path)
			params = {'package' : appx_path.name}
			appx_file = (appx_path.name, (appx_path.name, open(full_appx_path,'rb')))
			files.append(appx_file)

			# Get the dependency Framework packages
			# The dependencies are assumed to be in the top level
			# of the dir.
			full_deps_path = os.path.abspath(depsdir)
			for file in os.listdir(full_deps_path):
				file_path = pathlib.Path(os.path.join(full_deps_path,file))
				file_path.resolve()
				if( file_path.suffix == '.appx'):
					dep_file = (file_path.name, (file_path.name, file_path.open('rb')))
					files.append(dep_file)


			#DOIT
			response = session.post(request_url,
						verify=False,
						cookies=cookies,
						params=params,
						files=files)

def do_launch(ip, pfn, prid, **_args):
	scheme = 'https://'
	port = ''
	api = '/api/taskmanager/app?'
	request_url = scheme + ip + port + api

	with requests.Session() as session:
		cookie_filename = 'deployUtil.cookies'
		with open(cookie_filename,'r') as cookie_file:
			cookies = json.load(cookie_file)
			params = {
				'appid':base64.encodestring(bytes(prid, "utf-8")),
				'package':base64.encodestring(bytes(pfn, "utf-8"))
				}
			response = session.post(request_url,
						verify=False,
						cookies=cookies,
						params=params)
