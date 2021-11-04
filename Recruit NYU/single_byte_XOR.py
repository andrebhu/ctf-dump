import base64
a = "IConIT0xdSoldit1GTJ2GTIudRkxdigidTQgMyoZMXY0KiIZdiAZJTQ/NjJ2Zzs="
b = base64.b64decode(a)

for i in range(0, 255):
	c = ""
	for x in b:
		c += chr(i ^ int(x))
	if "flag" in c:
		print(c)