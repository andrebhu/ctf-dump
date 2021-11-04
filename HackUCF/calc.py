import requests

r = requests.get("http://ctf.hackucf.org:4000/calc/calc.php")
data = r.text[r.text.find("<expression>") + 12:r.text.find("</expression>")].replace("<br/>", " ")


cookie = r.cookies.get_dict()

response = int(eval(data))

c = {
	"answer": response
}
r = requests.post("http://ctf.hackucf.org:4000/calc/calc.php", data=c, cookies=cookie)
print(r.text)