import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Connected!\n')

fileName = str(input('file>'))

client.send(fileName.encode())

with open(fileName, 'wb') as file:
    while 1:
        data = client.recv(1000000000)
        if not data:
            break
        file.write(data)

print('Received!\n')
