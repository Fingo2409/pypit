#!/usr/local/bin/python3.9

import socket
import time
from _thread import *
from datetime import datetime as dt


def spam(client_socket, address):
    c_time = time.time()

    try:
        while True:
            time.sleep(5)
            client_socket.send("fail".encode())

    except socket.error as e:
        print(f"{dt.now().strftime('%H:%M:%S')} [\033[1;31m-\033[0;0m] {address[0]} connection closed after {round(time.time() - c_time)} seconds.")


def main():
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 22

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(0)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, address = s.accept()
        print(f"{dt.now().strftime('%H:%M:%S')} [\033[1;32m+\033[0;0m] {address[0]} is connected.")
        start_new_thread(spam, (client_socket, address, ))


if __name__ == "__main__":
    main()