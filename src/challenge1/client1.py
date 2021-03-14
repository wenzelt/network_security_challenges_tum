"""
challenge1 to receive exercises
"""

# pylint:disable=R0801
#!/usr/bin/env python3
import socket
from base64 import b64decode

# Fill in the right target here
HOST = "netsec.net.in.tum.de"
PORT = 20001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
sf = s.makefile("rw")  # we use a file abstraction for the sockets

data = sf.readline().rstrip("\n")
print("From Server: `{}'".format(data))

data = sf.readline().rstrip("\n")
print("From Server: `{}'".format(data))

data = input("Your Answer: ")
sf.write("{}\n".format(data))
sf.flush()

data = sf.readline().rstrip("\n")
print("From Server: `{}'".format(data))

data = input("Your Answer: ")
sf.write("{}\n".format(data))
sf.flush()

data = sf.readline().rstrip("\n")
print("From Server: `{}'".format(data))

data = sf.readline().rstrip("\n")
print("From Server: received {} bytes".format(len(data)))

data = b64decode(data)

PDF_HDR = b"%PDF-1.5"

if len(data) >= len(PDF_HDR) and data[: len(PDF_HDR)] == PDF_HDR:
    print("Looks like we got a PDF!")
    f = open("ex.pdf", "wb")
    f.write(data)
    f.flush()

sf.close()
s.close()
