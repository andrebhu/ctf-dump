from socket import socket

sock = socket()


for i in range(41, 100):
	sock = socket()
	sock.connect(('165.22.22.11', 9999))
	sock.recv(1024)
	sock.send(b">" * i + b".\n")
	sock.recv(1024)
	print(str(sock.recv(1024).strip()[-2:]), end="")
	sock.close()

#A

