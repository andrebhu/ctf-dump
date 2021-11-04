h = '1c0111001f010100061a024b53535009181c'
c = '686974207468652062756c6c277320657965'

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

h = bytes.fromhex(h)
c = bytes.fromhex(c)
b = byte_xor(h, c)

for i in b:
	print(str(hex(i))[2:], end="")
