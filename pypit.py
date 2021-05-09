#!/usr/bin/python3

import argparse
import logging
import socket
import time
from _thread import *
from datetime import datetime as dt


def get_args() -> argparse:
    parser = argparse.ArgumentParser(description="simple SSH tarpit")

    parser.add_argument("-p", "--port",
                        metavar="22",
                        type=int,
                        nargs=1,
                        action="store",
                        dest="port",
                        help="port to listen on (default 22)",
                        default=[22],
                        required=False)

    parser.add_argument("-t", "--time",
                        metavar="5",
                        type=int,
                        nargs=1,
                        action="store",
                        dest="time",
                        help="seconds to wait between connection checks (default 5)",
                        default=[5],
                        required=False)

    parser.add_argument("-l", "--logging",
                        action="store_true",
                        dest="logging",
                        help="if you want logging enabled (/var/log/pypit.log)",
                        default=False,
                        required=False)

    return parser.parse_args()


def activity(msg: str):
    now_time = dt.now().strftime('%H:%M:%S')
    print(f"{now_time} {msg}")
    if args.logging:
        logging.info(f"{now_time} {msg}")


def is_connected(client_socket: socket, address: str):
    c_time = time.time()  # get time when client is connected

    try:
        while True:
            client_socket.send("fail".encode())  # test if client is still connected
            time.sleep(args.time[0])             # and sleep for x seconds

    except socket.error:  # client is not connected anymore
        duration = round(time.time() - c_time)
        activity(f"[\033[1;31m-\033[0;0m] {address} connection closed after {duration} seconds.")


def main():
    if socket.has_ipv6:                     # if IPv6 is available
        server_host = "::"                  # set IPv6 host
        s = socket.socket(socket.AF_INET6)  # and IPv6 socket

    else:
        server_host = "0.0.0.0"
        s = socket.socket()

    s.bind((server_host, args.port[0]))
    s.listen()

    if args.logging:
        LOGFILE = "/var/log/pypit.log"
        logging.basicConfig(level=logging.DEBUG, filename=LOGFILE, filemode="a", format='%(message)s')

    activity(f"[*] Listening as {server_host}:{args.port[0]}")

    while True:
        client_socket, address = s.accept()
        address = address[0]  # address was (ip, port)

        if address.startswith("::ffff"):  # if IPv4 address
            address = address[7:]         # cut the first 7 letters

        activity(f"[\033[1;32m+\033[0;0m] {address} is connected.")
        start_new_thread(is_connected, (client_socket, address,))


if __name__ == "__main__":
    args = get_args()
    main()
