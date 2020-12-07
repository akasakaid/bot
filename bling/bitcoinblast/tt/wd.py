import requests,json,time,os,colorama
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
url = 'http://tuyulgaple.online/bitcoinblast/'
rd = 'https://us-central1-loaded-93189.cloudfunctions.net/redeemLoyaltyPoints_V2'
hd = {"Host": "tuyulgaple.online","Accept": "*/*","Content-Length": "78","Content-Type": "application/x-www-form-urlencoded"}
def wd(email,password):
	while True:
		try:
			a = {"tipe":"login","email":email,"password":password,"keys":""}
			b = json.dumps(a)
			c = r.post(url,headers=hd,data=b).text
			d = json.loads(c)["respon"]
			token = d["access_token"]
			hdw = {
			  	"Host": "us-central1-loaded-93189.cloudfunctions.net",
			  	"authorization": "Bearer "+token,
			  	"firebase-instance-id-token": "cd0AKiESLEs:APA91bFYUczPNpSwq7XLrA1d_Y5Q7c50Rddeg93FYmYT5g296e8V2_vBpgwSxc4FTuQopNlf0DZUhcvmN4hhuIN2ypplhtNI4tmSXH8Un2jGw9OwLMWWq04pMia8r1tG2wwNa-fzEHKk",
			  	"content-type": "application/json; charset=utf-8",
			  	"content-length": "104",
			  	"accept-encoding": "gzip",
			  	"user-agent": "okhttp/3.12.1"
			}
			dw = {"data":{"platform":"Android","email":email,"bundleid":"app.getloaded.bitcoinblast"}}
			data = json.dumps(dw)
			e = r.post(rd,headers=hdw,data=data).text
			f = json.loads(e)["result"]
			if f["success"] == False:
				print(f"[{biru}{email}{reset}]=[{merah}Sudah Melakukan Withdraw{reset}]=[{kuning}"+f["action"]+"]")
				break
			else:
				print(f"[{biru}{email}{reset}]=[{hijau}Success Melakukan Withdraw{reset}]=[{kuning}"+f["action"]+"]")
				break
		except Exception as e:
			continue
if os.name == 'nt':os.system("cls")
else:os.system("clear")
print("""
Program untuk membantu withdraw Bitcoin Blast

Traktir pembuat dengan segelas es teh di
https://trakteer.id/fowawaz
	""")
try:
	ap = open("akun.txt").readlines()
except IOError:
	print("File akun.txt Ora Ono!")
	exit()
print("Jumlah akun",len(ap))
print(" ")
for kamu in ap:
	akun = kamu.strip().split(" ")
	email = akun[0]
	password = akun[1]
	wd(email,password)
