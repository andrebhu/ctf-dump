import hashlib

f = open("colors.txt", "r")
colors = f.readlines()
for i in range(len(colors)):
	colors[i] = colors[i].lower().strip()

years = []
for i in range(3000):
	years.append(str(i).zfill(4))

neverlan = ["zestyfe", "durkinza", "purvesta", "s7a73farm"]

for a in colors:
	for b in years:
		for c in neverlan:
			s = a + "-" + b + "-" + c
			m = hashlib.md5()
			m.update(s.encode("utf-8"))
			if "267530778aa6585019c98985eeda255f" in m.hexdigest():
				print(s)
				break

