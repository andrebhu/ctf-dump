#!/usr/bin/env python3

from hashlib import sha512
from random import randint

class ahs512():

    def __init__(self, message):
        self.message = message
        self.key = self.generateKey()

    def generateKey(self):
        while True:
            key = randint(2, len(self.message) - 1)
            if len(self.message) % key == 0:
                break
        
        return key

    def transpose(self, message):
        transposed = [0 for _ in message]

        columns = len(message) // self.key

        for i, char in enumerate(message):
            row = i // columns
            col = i % columns
            transposed[col * self.key + row] = char

        return bytes(transposed)

    def rotate(self, message):
        return [((b >> 4) | (b << 3)) & 0xff for b in message]

    def hexdigest(self):
        transposed = self.transpose(self.message)
        print(transposed)
        rotated = self.rotate(transposed)
        return sha512(bytes(rotated)).hexdigest()

original_message = b"pumpkin_spice_latte!"
print(len(original_message))
original_digest = ahs512(original_message).hexdigest()
print(original_digest)

original_message2 = "pumpkin_spice_latte!".encode()
print(len(original_message2))
original_digest2 = ahs512(original_message2).hexdigest()
print(original_digest2)