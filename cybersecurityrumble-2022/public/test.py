#!/usr/bin/env python3

from urllib.parse import parse_qs, urlencode
from Crypto.Cipher import AES
from Crypto.Hash import HMAC
from Crypto.Util.Padding import pad, unpad

INSTANCE_KEY = "abababababababababababababababac".encode()

def serialize_user(user):
    data = urlencode(user).encode()
    # add default IV, which is obtainable
    aes = AES.new(INSTANCE_KEY, AES.MODE_CBC, iv=b"\x0c\x8c\x16\xc5\x99\x91\xd7\x96x'\xa02U\xf8\xd1\xcd")
    ct = aes.encrypt(pad(data, 16))
    # guarantee ciphertext integrity
    mac = HMAC.new(INSTANCE_KEY, ct).digest()
    print(aes.iv)
    print(ct)
    print(mac)
    return (aes.iv + ct + mac).hex()

print(serialize_user({"user": "stduser", "role": "premium"}))

def deserialize_user(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    iv, ct, mac = ciphertext[:16], ciphertext[16:-16], ciphertext[-16:]

    # Check ciphertext integrity
    if not HMAC.new(INSTANCE_KEY, ct).digest() == mac:
        raise ValueError("Ciphertext was manipulated.")

    aes = AES.new(INSTANCE_KEY, AES.MODE_CBC, iv=iv)
    plaintext = unpad(aes.decrypt(ct), 16)
    user_obj_raw = parse_qs(plaintext.decode())
    user_obj = {k: v[0] for k, v in user_obj_raw.items()}

    return user_obj