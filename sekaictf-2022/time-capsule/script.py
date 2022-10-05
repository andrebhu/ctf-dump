#!/usr/bin/env python3

import random
import itertools
'''
encrypted flag is 61 bytes long
seed is 18 bytes

flag message is 43 bytes long?
'''

def reverse(message, key):
    res = [""] * len(message)

    idx = 0
    for i in key:
        for j in range(i, len(message), len(key)):
            res[j] = message[idx]
            idx += 1

    return "".join(res)
        

def crack(message):
    for key in itertools.permutations([i for i in range(8)], 8):
        m = message
        for _ in range(42):
            m = reverse(m, key)

        if 'SEKAI{' in m:
            print(m)
            break


if __name__ == "__main__":
    with open("flag.enc", "rb") as file:
        data = [int(b) for b in bytes(file.read())]
        # reversing stage 2
        # reverse seed/key
        seed = [chr(d ^ 0x42) for d in data]
        random.seed("".join(seed[-18:]))
        
        # create key
        key = [random.randrange(256) for _ in range(43)]

        message = [chr(data[i] ^ key[i]) for i in range(len(key))]

        # reverse stage 1
        crack(message)