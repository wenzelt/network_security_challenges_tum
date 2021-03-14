"""
Client for challenge 2 of exercise
"""
# !/usr/bin/env python3
import socket
from base64 import b64decode
from random import randrange

from src.util.helpers import double_digits_from_randnum,eval_expr

while True:
    HOST = "netsec.net.in.tum.de"
    PORT = 20002

    USERNAME = "root"
    PASSWORD = f"Password{double_digits_from_randnum(randrange(0, 100))}"
    credentials = USERNAME + "," + PASSWORD

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    sf = s.makefile("rw")  # we use a file abstraction for the sockets

    sf.write("{}\n".format(credentials))
    sf.flush()

    math_expr = sf.readline().rstrip("\n")

    print("Solve the following equation to prove you are human: ", math_expr)
    response = eval_expr(math_expr)
    sf.write("{}\n".format(response))
    sf.flush()

    data = sf.readline().rstrip("\n")
    print("From Server: `{}'".format(data))

    data = sf.readline().rstrip("\n")
    print("From Server: received {} bytes".format(len(data)))
    print(".")
    data = b64decode(data.encode())

    PDF_HDR = b"%PDF-1.5"

    if len(data) >= len(PDF_HDR) and data[: len(PDF_HDR)] == PDF_HDR:
        print("Looks like we got a PDF!")
        f = open("ex2.pdf", "wb")
        f.write(data)
        f.flush()
        break

sf.close()
s.close()
