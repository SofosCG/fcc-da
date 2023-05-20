#!/usr/bin/pyton3

import socket

clientsocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.68.100'
host = socket.gethostname()

port = 444

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
