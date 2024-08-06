import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))

server.listen(30)

while True:
    client, addr = server.accept()
    print("connected to Client")
    print(client.recv(1024).decode())
    client.send("Hello World From Server".encode())
    client.close()
