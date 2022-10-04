#!/usr/bin/env python3

import hashlib
from socket import socket


def retrieve_info():
    s = socket()
    s.connect(('challs.ctf.sekai.team', 3001))

    data = s.recv(2048).split(b"\n")

    secret = data[0].decode()
    enc = [d.replace("[","").replace("]","").replace(" ","") for d in data[1].decode().split("],")]
    enc = [e.split(",") for e in enc]
    enc = [[int(i) for i in e] for e in enc]

    return bytes.fromhex(secret), enc


def gen_pubkey(secret: bytes, hasher=hashlib.sha512) -> list:
    def hash(m): return hasher(m).digest()
    state = hash(secret)
    pubkey = []
    for _ in range(len(hash(b'0')) * 4):
        pubkey.append(int.from_bytes(state, 'big'))
        state = hash(state)
    return pubkey


def happiness(x: int) -> int:
    return x - sum((x >> i) for i in range(1, x.bit_length()))

if __name__ == "__main__":
    secret, enc = retrieve_info()
    A = gen_pubkey(secret, hashlib.sha256)

    differences = []
    for e in enc:
        l = []
        for i in range(len(e)):
            # print(happiness(A[i]), happiness(e[i]))
            l.append(happiness(A[i]) - happiness(e[i]))
        differences.append(l)

    for d in differences:
        print(d)
    