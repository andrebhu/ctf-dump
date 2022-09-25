#!/usr/bin/env python3

import binascii

def hexstr_to_intarr(h: str):
    return [int(h[i:i+2], 16) for i in range(0, len(h), 2)]

def intarr_to_hexstr(arr: list):
    return "".join([hex(a)[2:] for a in arr])

def intarr_to_str(arr: list):
    return "".join([chr(a) for a in arr])

def xor(arr1: list, arr2: list):
    return [arr1[i] ^ arr2[i] for i in range(len(arr2))]


if __name__ == "__main__":
    cipher_1 = open("c1.txt", "r").read()
    cipher_2 = open("c2.txt", "r").read()

    cipher_1 = [hexstr_to_intarr(cipher_1[i:i+32]) for i in range(0, len(cipher_1), 32)]
    cipher_2 = [hexstr_to_intarr(cipher_2[i:i+32]) for i in range(0, len(cipher_2), 32)]

    plain_b1 = binascii.hexlify(b"Decrypt this... ").decode()
    plain_b1 = hexstr_to_intarr(plain_b1)

    inter_1p = xor(plain_b1, cipher_2[0])
    plain_b2 = xor(inter_1p, cipher_1[1])

    temp = plain_b2
    for i in range(1, 48):
        inter_ip = xor(temp, cipher_2[i])
        plain_bi = xor(inter_ip, cipher_1[i + 1])
        temp = plain_bi
        print(intarr_to_str(plain_bi), end="")
