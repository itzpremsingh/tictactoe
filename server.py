from socket import AF_INET, SOCK_STREAM

from config import HOST, PORT
from helper import server_starter, socket


def server_handler() -> None:
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen()

    print("Server started")

    server_starter(server)

    server.close()
