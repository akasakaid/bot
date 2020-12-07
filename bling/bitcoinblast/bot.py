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
		token = d["access_token"]
		uid = d["user_id"]
		usr = {"tipe":"userprofil","token":token,"uid":uid,"keys":""}
		dusr = json.dumps(usr)
		clm = {"tipe":"misi","token":token,"uid":uid,"keys":""}
		dclm = json.dumps(clm)
		e = r.post(url,headers=hd,data=dusr).text
		f = json.loads(e)
		print(f["respon"].replace("\u001b[37m","").replace("\u001b[92m","").replace("\u001b[36m",""))
		while True:
			g = r.post(url,headers=hd,data=dclm).text
			h = json.loads(g)
			if h["respon"] == '\x1b[37mMaximum loyalty points have been earned':
				print("Maximum loyalty points have been earned")
				break
			else:
				print(h["respon"].replace("\x1b[34m","").replace("\x1b[36m","").replace("\x1b[37m","").replace("\x1b[92m","").replace("\x1b[36m",""))
				tunggu(30)
	except requests.exceptions.ConnectionError:
		print("Koneksi Error!!")
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print("Bermain Bitcoin Blast dan Bitcoin Blocks\n")

try:
	ap = open("akun.txt").readlines()
	print(len(ap))
	for kamu in ap:
	 akun = kamu.strip().split(" ")
	 email = akun[0]
	 password = akun[1]
	 print(f"[Akun]======[{email}]")
	 #nuyul(email,password)
except IOError:
	print("File akun.txt Ora Ono!")