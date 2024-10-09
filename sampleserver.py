import socket as s
from threading import Thread

HOST = '127.0.0.1'
PORT = 3075
class ASPIncomingThread(Thread):
    def __init__(self, conn, addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr = addr
        print("Thread {}:{} started....".format(addr[0],addr[1]))
    def run(self):
        self.conn.sendall("Hi This is Sanjay\n".encode())
        data = conn.recv(1024)
        while data:
             print("{}: ".format(self.addr[0])+ data.decode(), end="")
             data = conn.recv(1024)
sck = s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST, PORT))
sck.listen()
while True:
    print("Waiting for New Connection")
    conn,addr = sck.accept()
    print("Connection received from {}:{}".format(addr[0],addr[1]))
    ASPIncomingThread(conn,addr).start()
