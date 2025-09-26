from sys import argv

from client import client_handler
from server import server_handler

if len(argv) != 2 or argv[1] not in {"server", "client"}:
    print("Usage: python main.py [server|client]")
    quit(1)

if argv[1] == "server":
    server_handler()

elif argv[1] == "client":
    client_handler()
