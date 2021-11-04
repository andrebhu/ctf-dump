from pwn import *

r = remote('ctf.hackucf.org', 10102)
r.recvuntil("\n")
r.recvuntil("\n")
s = r.recv()

values = []
while "flag" not in s:
	print(s)
	a = ""
	if "first" in s:
		r.send(values[0] + "\n")
		pass		

	for i in s:
		if i.isdigit():
			a += i
	r.send(a + "\n")
	values.append(a)	
	s = r.recv()
print(s)
