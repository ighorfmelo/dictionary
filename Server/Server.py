import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7777))

print('Listen on 7777')

server.listen(1)

connection, address = server.accept()

fileName = connection.recv(1024).decode()

with open(fileName, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print('File sended')