from socket import socket
from Crypto.Util.number import inverse, long_to_bytes
import base64
import string
import codecs

sock = socket()
sock.connect(('socket.cryptohack.org', 13377))

while True:
	data = sock.recv(1024)
	if b"crypto{" in data:
		print(data)
		break

	if b"Invalid" in data:
		break

	else:
		print(data.decode('utf-8').strip())
		data = data.split(b', "encoded": "')
		response = b'{"decoded": "'


		if b"base64" in data[0]:
			response += base64.b64decode(data[1][:-3]) + b'"}\n'

		elif b"hex" in data[0]:
			response += long_to_bytes(int(b"0x" + data[1][:-3], 16)) + b'"}\n'

		elif b"rot13" in data[0]:
			rot = codecs.encode(data[1].decode("utf-8"), "rot13")
			response += rot.encode("utf-8")

		elif b"bigint" in data[0]:
			response += long_to_bytes(int(data[1][:-3], 16)) + b'"}\n'

		elif b"utf-8" in data[0]:
			data = data[0].split(b'"encoded": ')
			data = data[1][1:-3].decode("utf-8").split(", ")
			a = b""
			for c in data:
				a += chr(int(c)).encode("utf-8")
			response += a + b'"}\n'
			
		print(response.decode("utf-8").strip())
		sock.send(response)


