from collections import namedtuple

opt = namedtuple("opt",['switch','help'])

# common options
ip = opt(	switch='-ip',
		help='ip args help')

# pair command and options
pair = opt(	switch='pair',
		help='pair command help')

pin = opt(	switch='-pin',
		help='pin arg help')

# list command and options
list = opt(	switch='list',
		help='list command help')

pretty = opt(	switch='-pretty',
		help='pretty arg help')

# install command and options
inst = opt(	switch='install',
		help='install command help')

deps = opt(	switch='--depsdir',
		help='dependencies directory help')

appx = opt(	switch='appx',
		help='appx help')

# uninstall command and options
uninst = opt(	switch='uninstall',
		help='uninstall command help')

pfn = opt(	switch='-pfn',
		help='package full name arg help')

# launch command and options
launch = opt(	switch='launch',
		help='launch command help ')

tool_desc = \
""" Provides command line access to developer features exposed by the Windows
Device Portal including, pairing with devices, managing applications, and
managing processes on devices.
""" 
