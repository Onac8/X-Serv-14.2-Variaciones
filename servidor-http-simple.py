#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1235))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(2048))
        print ('Answering back...')
        recvSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n' +
            '<html><body><h1>WINTER IS COMING</h1>' +
            '<img src="http://cdn.playbuzz.com/cdn/2bfd334d-a2dc-48da-a14b-f15e8bd223c6/22540de3-ba97-497e-8e11-ccac96e2967b.jpg"' +
            'alt="Got_Houses" style="width:1000px;height:300px;">' +
            '<iframe width="800" height="400" src="https://www.youtube.com/embed/ECewrAld3zw" frameborder="0" allowfullscreen></iframe>' +
            '</body></html>' +
            '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
