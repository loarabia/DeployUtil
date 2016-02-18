# DeployUtil
DeployUtil is a command-line tool and a library to be integrated into other tools for performing Universal Windows Application development oriented tasks using the Windows Device Portal. 

Currently, it supports:

1. authenticating a PC (or Mac or Linux box) to a target Windows 10 development device
2. list installed application on the target
3. install an application on the target
4. uninstall an application on the target
5. launch an application on the taget

## Status: Pre-Alpha
The current code quality is pre-alpha which means its really sample code to give you an idea of what REST APIs to call. There is a lot of work to do on handling common error flows, documentation, and just making the usability of the tool better (for instance the list command returns a huge set of things that you then need to dig through it would be nice to have a search command that would narrow that down).

## Dependencies
This project has the following dependencies:

1. [Python 3](https://www.python.org/)
2. [requests lib](http://docs.python-requests.org/en/master/)

## Usage
```bash
python .\DeployUtil --help
```
or just
```bash
./DeployUtil --help
```
