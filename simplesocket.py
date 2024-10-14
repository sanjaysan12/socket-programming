import socket as s
import threading
HOST = '0.0.0.0'
PORT = 3074

sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))
sck.listen()

conn , addr = sck.accept()
data = conn.recv(1024)
while data:
    print(data.decode())
    data = conn.recv(1024)
