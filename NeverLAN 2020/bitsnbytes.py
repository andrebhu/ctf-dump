import requests
import time
import datetime
while True:
	url = "https://challenges.neverlanctf.com:1150/svg.php"
	s = ""
	r = requests.get(url)
	a = r.text.split("\n")[2].split("><")
	for line in a:
		if "#00ff00" in line:
			s += "0"
		elif "#333136" in line:
			s += "1"
	s = ''.join([(chr(int(s[i:i+8], 2))) for i in range(0, len(s), 8)])
	print(s)
	if 'flag' in s:
		print("FLAG!")
		break
	time.sleep(10)


