#!/usr/bin/env python3

import time
import os
import random

# from SECRET import flag
flag = "SEKAI{testingmorebytes}"

def encrypt_stage_one(message, key):
    print(f"Message: {message} Key: {key}")
    u = [s for s in sorted(zip(key, range(len(key))))]
    res = ''
    
    print(f"u: {u}")

    for i in u:
        for j in range(i[1], len(message), len(key)):
            res += message[j]

    return res

def encrypt_stage_two(message):
    now = str(time.time()).encode('utf-8')
    now = now + "".join("0" for _ in range(len(now), 18)).encode('utf-8')

    print(f"now length: {len(now)}")
    print(now)
    
    
    random.seed(now)
    key = [random.randrange(256) for _ in message]

    print("Key: ")
    print(key)
    
    return [m ^ k for (m,k) in zip(message + now, key + [0x42]*len(now))]


# I am generating many random numbers here to make my message secure
rand_nums = []
while len(rand_nums) != 8:
    tmp = int.from_bytes(os.urandom(1), "big")
    if tmp not in rand_nums:
        rand_nums.append(tmp)

print(f"rand_nums: {rand_nums}")

for _ in range(42):
    # Answer to the Ultimate Question of Life, the Universe, and Everything...
    flag = encrypt_stage_one(flag, rand_nums)


print(f"Flag after stage 1: {bytes(flag.encode())}")


# Another layer of randomness based on time. Unbreakable.
# res = encrypt_stage_two(flag.encode('utf-8'))


# print(res)
# print(bytes(res))
# with open("flag.enc", "wb") as f:
#     f.write(bytes(res))
# f.close()
