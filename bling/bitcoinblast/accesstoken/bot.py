import requests,json,time,os
r = requests.Session()
def tunggu(t):
	while t:
		wd='# Jeda selama '+str(t)+" detik "
		print(wd,end='\r',flush=True)
		time.sleep(1)
		t -= 1
url = 'http://tuyulgaple.online/bitcoinblast/'
hd = {"Host": "tuyulgaple.online","Accept": "*/*","Content-Length": "78","Content-Type": "application/x-www-form-urlencoded"}
def nuyul(email,password):
	try:
		a = {"tipe":"login","email":email,"password":password,"keys":""}
		b = json.dumps(a)
		c = r.post(url,headers=hd,data=b).text
		d = json.loads(c)["respon"]
		token = d["refresh_token"]
		print(token)
	except requests.exceptions.ConnectionError:
		print("Koneksi Error!!")

print("NGAMBIL ACCESS TOKEN\n")

try:
	ap = open("akun.txt").readlines()
	for kamu in ap:
	 akun = kamu.strip().split(" ")
	 email = akun[0]
	 password = akun[1]
	 nuyul(email,password)
except IOError:
	print("File akun.txt Ora Ono!")