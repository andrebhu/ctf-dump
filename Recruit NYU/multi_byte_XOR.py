import base64
string = "JR4YFw8YLwA7Jx0mCRsaGBsMKhwSLwMdLhsBMC0YHBgwMwcBMBcmFBsfIjAHKxMVHBEBIAoXfA8="
decoded = base64.b64decode(string)

key = "_"
charset = "ABCEFGHIJLKMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789}{"

flag = "flag{w"
#ends with r
#Crypt
r  = ""



def xor(str1, str2):
	s1 = bytearray(str1)
	s2 = bytearray(str2)

	result = bytearray()

	for i in range(len(s2)):
		result.append(s1[i%len(s1)] ^ s2[i])
	return str(result)

print(xor(flag, decoded))
