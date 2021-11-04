from pwn import *

r = remote('ctf.hackucf.org', 10101)
r.recvuntil("\n")
r.recvuntil("\n")
s = r.recv()


while "flag" not in s:
	a = ""
	for i in s:
		if i.isdigit():
			a += i
	r.send(a + "\n")	
	s = r.recv()
print(s)
