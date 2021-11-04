

from pwn import *
r = remote('ctf.hackucf.org', 10104)
r.recvuntil("\n")
r.recvuntil("\n")
s = r.recv()

while "flag" not in s:
	a = str(int(eval(s[:len(s)-2])))
	r.send(a + "\n")	
	s = r.recv()
print(s)
