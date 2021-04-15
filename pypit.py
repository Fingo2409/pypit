#!/usr/bin/python3.9

import logging
import socket
import time
from _thread import *
from datetime import datetime as dt


def spam(client_socket, address):
    c_time = time.time()  # get time when client is connected

    try:
        while True:
            client_socket.send("fail".encode())  # test if client is still connected
            time.sleep(5)

    except socket.error:
        now_time = dt.now().strftime('%H:%M:%S')
        duration = round(time.time() - c_time)
        logging.info(f"{now_time} [\033[1;31m-\033[0;0m] {address} connection closed after {duration} seconds.")


def main():
    LOGFILE = "/var/log/pypit.log"
    SERVER_PORT = 22

    if socket.has_ipv6:                     # if IPv6 is available
        SERVER_HOST = "::"                  # set IPv6 host
        s = socket.socket(socket.AF_INET6)  # and IPv6 socket

    else:
        SERVER_HOST = "0.0.0.0"
        s = socket.socket()

    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen()

    logging.basicConfig(level=logging.DEBUG, filename=LOGFILE, filemode="a", format='%(message)s')
    logging.info(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, address = s.accept()
        address = address[0]  # address was (IP, PORT)

        if address.startswith("::ffff"):  # if IPv4 address
            address = address[7:]         # cut the first 7 letters

        now_time = dt.now().strftime('%H:%M:%S')
        logging.info(f"{now_time} [\033[1;32m+\033[0;0m] {address} is connected.")

        start_new_thread(spam, (client_socket, address,))


if __name__ == "__main__":
    main()
