#!/usr/bin/env python3

from Crypto.Hash import HMAC
from itertools import permutations
from Crypto.Util.Padding import pad, unpad
from urllib.parse import parse_qs, urlencode

plaintext = {
    "user": "stduser",
    "role": "pleb"
    }

cookie = "7da4cf5704e89244578c7f316c9658d1085bf8127ab0b8e4c0ea85504fc68461e3c74bb56aa71437f33cd24f1b724af14ed18315c47acd73728ad4c6ec74903f"
cookie = bytes.fromhex(cookie)
iv, ct, mac = cookie[:16], cookie[16:-16], cookie[-16:]
charset = [chr(i) for i in range(256)]




def generate_hash(key):
    mac = HMAC.new(key, ct).digest()
    return mac

def create_keys(length):
    return permutations(charset, length)


LENGTH = 16

for i in range(1, LENGTH):
    keys = create_keys(i)
    print(f"Bruteforcing length {i}")
    for k in keys:
        a = "".join(k).encode() # key to bytestring
        h = generate_hash(a)
        if h == mac:
            print(a)
            break
