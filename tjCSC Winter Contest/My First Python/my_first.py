flag = open('flag.txt', 'r').read()

n = len(flag)
flag = zip(flag[:n//2], flag[n//2:])

for i, j in flag:
	print(ord(i))
	print(ord(j))