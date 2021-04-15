#!/usr/local/bin/python3.9

import logging
import socket
import time
from _thread import *
from datetime import datetime as dt


def spam(client_socket, address):
    c_time = time.time()  # get starting time

    try:
        while True:
            time.sleep(5)
            client_socket.send("fail".encode())  # test if client is still connected

    except socket.error:
        logging.info(f"{dt.now().strftime('%H:%M:%S')} [\033[1;31m-\033[0;0m] {address} connection closed after {round(time.time() - c_time)} seconds.")


def main():
    logging.basicConfig(level=logging.DEBUG, filename="/var/log/pypit.log", filemode="w", format='%(message)s')

    SERVER_HOST = "::"
    SERVER_PORT = 22

    s = socket.socket(socket.AF_INET6)
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen()
    logging.info(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, address = s.accept()
        address = address[0]
        if address.startswith("::ffff"):
            address = address[7:]

        logging.info(f"{dt.now().strftime('%H:%M:%S')} [\033[1;32m+\033[0;0m] {address} is connected.")
        start_new_thread(spam, (client_socket, address, ))


if __name__ == "__main__":
    main()
