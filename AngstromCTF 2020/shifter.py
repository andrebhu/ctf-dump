from socket import socket


def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074]

sock = socket()
sock.connect(('misc.2020.chall.actf.co', 20300))
s = ""
s = sock.recv(1024).decode("utf-8")
while True:
	print(s)
	s = s[s.index("Shift") + 6:-2].strip().split(" by n=")

	sock.send(encrypt(s[0], fib[int(s[1])]).encode("utf-8") + b"\n")
	s =  sock.recv(1024).decode("utf-8")

	if "actf" in s:
		print(s)
		break

