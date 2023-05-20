#!/usr/bin/pyton3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.68.100'
host = socket.gethostbyname()
port = 444

#Binding the socket
serversocket.bind((host, port))

#Starting TCP listner
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()
    
    print("Received connection from " % str(address))
    
    message = "Hello! Thank you for connecting to the server" + "\r\n"
    
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()
