#!/usr/bin/env python3
import socket
import time
from base64 import b64encode, b64decode

HOST = "thisisno.valid.hostname"
PORT = 42

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

buf = s.recv(1024)
print(buf.decode())

triforce = input("Enter a clean triforce:")
print("Given Input:\n{}".format(triforce))

print("Sending...", flush=True)
# TODO you should send your triforce here

sf = s.makefile("rw")
buf = sf.readline().rstrip("\n")
print(buf)

data = sf.readline().rstrip("\n")
print("From Server: received {} bytes".format(len(data)))

data = b64decode(data.encode())

pdf_hdr = b"%PDF-1.5"

if len(data) >= len(pdf_hdr) and data[: len(pdf_hdr)] == pdf_hdr:
    print("Looks like we got a PDF!")

sf.close()
s.close()
