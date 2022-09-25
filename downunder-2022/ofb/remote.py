#!/usr/bin/env python3

import binascii
from socket import socket

def hexstring_to_intarray(h: str):
    return [int(h[i:i+2], 16) for i in range(0, len(h), 2)]

def intarray_to_hexstring(arr: list):
    return "".join([hex(a)[2:] for a in arr])
        
if __name__ == "__main__":
    s = socket()
    s.connect(('2022.ductf.dev', 30009))
    s.recv(1024) # iv: 
    s.send(b'00000000000000000000000000000000\n') # all 0s

    data = s.recv(2048).split(b"\n")
    cipher_1 = data[0].decode()

    c1 = open("c1.txt", "w")
    # print("Cipher 1:", cipher_1)
    c1.write(cipher_1)
    c1.close()

    plain_b1 = [ord(c) for c in "Decrypt this... "]
    cipher_b1 = hexstring_to_intarray(cipher_1[:32])
    inter_b1 = [plain_b1[i] ^ cipher_b1[i] for i in range(16)]

    print(f"Sending {intarray_to_hexstring(inter_b1)}")
    s.send(intarray_to_hexstring(inter_b1).encode() + b"\n") # sending second iv
    data = s.recv(2048)
    # print("Cipher 2:", data.decode())
    c2 = open("c2.txt", "w")
    c2.write(data.decode().strip())
    c2.close()