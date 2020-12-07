import requests,json,time,os,sys
r = requests.Session()
from colorama import *
init(autoreset=True)
merah = Fore.RED+Style.BRIGHT
hitam = Fore.BLACK+Style.BRIGHT
hijau = Fore.GREEN+Style.BRIGHT
kuning = Fore.YELLOW+Style.BRIGHT
biru = Fore.BLUE+Style.BRIGHT
magenta = Fore.MAGENTA+Style.BRIGHT
cyan = Fore.CYAN+Style.BRIGHT
putih = Fore.WHITE+Style.BRIGHT
reset = Fore.RESET+Style.RESET_ALL
def tunggu(t):
	while t:
		wd='# Jeda selama '+str(t)+" detik "
		print(wd,end='\r',flush=True)
		time.sleep(1)
		t -= 1
url = 'http://tuyulgaple.online/bitcoinblast/'
bl1 = 'https://us-central1-loaded-93189.cloudfunctions.net/levelComplete'
bl2 = 'https://us-central1-loaded-93189.cloudfunctions.net/userRewardConfig'
hd = {"Host": "tuyulgaple.online","Accept": "*/*","Content-Length": "78","Content-Type": "application/x-www-form-urlencoded"}
mbl2 = {"data": {"platform": "Android","bundleid": "com.bling.bitcoinblocks"}}
databl2 = json.dumps(mbl2)
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
				i = r.post(bl2,data=databl2,headers={"Host": "us-central1-loaded-93189.cloudfunctions.net","accept": "*/*","authorization": "Bearer "+token,"content-type": "application/json; charset=utf-8","user-agent": "okhttp/3.12.1","content-length": "68"})
				j = r.post(bl1,data=databl2,headers={"Host": "us-central1-loaded-93189.cloudfunctions.net","accept": "*/*","authorization": "Bearer "+token,"content-type": "application/json; charset=utf-8","user-agent": "okhttp/3.12.1","content-length": "68"}).text
				k = json.loads(j)["result"]
				if k["message"] == "Maximum loyalty points have been earned. Come back tomorrow to continue earning loyalty points.":
					print("Maximum loyalty points have been earned.")
					break
				else:
					print(k["message"])
					tunggu(10)
			else:
				print(h["respon"].replace("\x1b[34m","").replace("\x1b[36m","").replace("\x1b[37m","").replace("\x1b[92m","").replace("\x1b[36m",""))
				tunggu(10)
	except requests.exceptions.ConnectionError:
		print("Koneksi Error!!")
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print("Bermain Bitcoin Blast dan Bitcoin Blocks\n")

try:
	ap = open("akun.txt").readlines()
	print("Jumlah Akun:",len(ap),'\n')
	for kamu in ap:
	 akun = kamu.strip().split(" ")
	 email = akun[0]
	 password = akun[1]
	 print(f"[Akun]======[{email}]")
	 nuyul(email,password)
except IOError:
	print("File akun.txt Ora Ono!")
