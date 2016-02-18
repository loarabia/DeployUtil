#This code is licensed under the "MIT License" see LICENSE.txt
""" This contains all of the definitions for the commandline arguments as
named tuples.
"""
from collections import namedtuple

argument = namedtuple("argument", ['switch', 'help'])

# common options
ip = argument(switch='-ip',
              help='ip args help')

# pair command and options
pair = argument(switch='pair',
                help='pair command help')

pin = argument(switch='-pin',
               help='pin arg help')

# list command and options
list = argument(switch='list',
                help='list command help')

pretty = argument(switch='-pretty',
                  help='pretty arg help')

# install command and options
inst = argument(switch='install',
                help='install command help')

deps = argument(switch='--depsdir',
                help='dependencies directory help')

appx = argument(switch='appx',
                help='appx help')

# uninstall command and options
uninst = argument(switch='uninstall',
                  help='uninstall command help')

pfn = argument(switch='-pfn',
               help='package full name arg help')

prid = argument(switch='-prid',
                help='package relateve id help')

# launch command and options
launch = argument(switch='launch',
                  help='launch command help ')

tool_desc = \
""" Provides command line access to developer features exposed by the Windows
Device Portal including, pairing with devices, managing applications, and
managing processes on devices.
"""
