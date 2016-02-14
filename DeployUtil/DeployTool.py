#
# Command line wrapper for using WDP to install, uninstall,
# enumerate, and launch applications
# 
# But first time you use it, you have to set up a pin

import urllib.request
import base64

default_http_port = 10080
default_https_port = 10443
default_http_domain = "http://localhost"
default_https_domain = "https://localhost"

def handle_cmdline_args():
	"""
	Parses the commandline arguments
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument()

# Remote Deploy
def main():
	pass

def do_install_app():
	pass

def do_uninstall_app():
	pass

def do_enumerate_installed_apps():
	# /api/app/packagemanager/packages?_=1455257047427
	installed_apps_request = urllib.request.Request(
		url="http://localhost:10080/api/app/packagemanager/packages?",
		method="GET")
	installed_apps_response = urllib.request.urlopen(installed_apps_request)
	print(installed_apps_response.read())

def do_launch_app():
	pass

def do_handle_pin(pin):
	installed_apps_request = urllib.request.Request(
		url="http://localhost:10080/api/app/authorize/pair?pin={0}".format(pin),
		method="POST")
	installed_apps_response = urllib.request.urlopen(installed_apps_request)
	print(installed_apps_response.read())
	pass
