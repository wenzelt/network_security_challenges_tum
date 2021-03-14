#!/usr/bin/env python3
import socket
from base64 import b64decode
from random import randrange

from src.util import double_digits_from_randnum

while True:
    HOST = "netsec.net.in.tum.de"
    PORT = 20002

    username = "root"
    password = f"Password{double_digits_from_randnum(randrange(0, 100))}"
    credentials = username + "," + password

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    sf = s.makefile("rw")  # we use a file abstraction for the sockets

    sf.write("{}\n".format(credentials))
    sf.flush()

    challenge = sf.readline().rstrip("\n")

    print("Solve the following equation to prove you are human: ", challenge)
    response = eval(challenge)
    sf.write("{}\n".format(response))
    sf.flush()

    data = sf.readline().rstrip("\n")
    # print("From Server: `{}'".format(data))

    # data = sf.readline().rstrip('\n')
    # print("From Server: received {} bytes".format(len(data)))
    print(".")
    data = b64decode(data.encode())

    pdf_hdr = b"%PDF-1.5"

    if len(data) >= len(pdf_hdr) and data[: len(pdf_hdr)] == pdf_hdr:
        print("Looks like we got a PDF!")
        f = open("ex2.pdf", "wb")
        f.write(data)
        f.flush()
        break

    sf.close()
    s.close()
