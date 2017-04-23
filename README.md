# fuzzbunch_wrapper
Fuzzbunch Cli->Wine->fb.py wrapper

#Dependencies:
regular fuzzbunch dependencies installed in wine
install fuzzbunch this way: https://github.com/knightmare2600/ShadowBrokers/tree/master/Lost_In_Translation

Set Wine's PATH environment variable to c:\[fuzzbunch-path]\windows\lib\x86-Windows

#Usage:

./fbcli.py module|list

./fbcli.py eternalblue --targetip 1.1.1.1

./fbcli.py doublepulsar --help

./fbcli.py doublepulsar --targetip 1.1.1.1 --function ping
