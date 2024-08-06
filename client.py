import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(("localhost", 9999))

socket.send("Hello World From Client".encode())
print(socket.recv(1024).decode())