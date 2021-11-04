import base64
f = open("encrypted_db", "r")
lines = f.readlines()
d = ""
for i in lines:
	d += bytearray.fromhex(i).decode()
d = base64.b64decode(d)
print(d)