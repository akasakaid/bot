# tidak semua code ini murni dari saya sendiri saya juga mengambil beberapa code program ini dari sourcode program lain
# terimakasih yang sebesar besarnya kepada semua orang yang terlibat dalam pembuatan program ini yang tidak saya bisa sebutkan satu per satu
# ttd : AkasakaID

import requests,json,time,os,random
r = requests.Session()
acc = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyCbnj6yOAYLoy5XJCSXf4r8h8_v11oLXYA'
gtoken = 'https://securetoken.googleapis.com/v1/token?key=AIzaSyCbnj6yOAYLoy5XJCSXf4r8h8_v11oLXYA'
bl1 = 'https://us-central1-loaded-93189.cloudfunctions.net/levelComplete'
bl2 = 'https://us-central1-loaded-93189.cloudfunctions.net/userRewardConfig'
merah = '\x1b[1;31m'
hijau = '\x1b[1;32m'
kuning = '\x1b[1;33m'
biru = '\x1b[1;34m'
magenta = '\x1b[1;35m'
cyan = '\x1b[1;36m'
putih = '\x1b[1;37m'
def tunggu(t):
	while t:
		wd=f'{putih}# Jeda selama '+str(t)+" detik "
		print(wd,end='\r',flush=True)
		time.sleep(1)
		t -= 1
		
def countdown(t):
    while t:
        m, s= divmod(t,60)
        h, m = divmod(m,60)
        time_left="#Next GAME in  Hour ["+str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)+"]"
        print(time_left, end='\r', flush=True)
        time.sleep(1)
        t -= 1

hd = {
"Content-Type": "application/json",
"X-Firebase-Locale": "",
"X-Client-Version": "Android/GmsCore/X19002000/FirebaseCore-Android",
"Accept-Language": "en-US",
"X-Android-Package": "com.bling.bitcoinblocks",
"X-Android-Cert": "E998BC4F040DCA2383FAEB36E3FE5A629C31B790",
"X-Goog-Spatula": "CjcKF2NvbS5ibGluZy5iaXRjb2luYmxvY2tzGhw2Wmk4VHdRTnlpT0QrdXMyNC81YVlwd3h0NUE9GKvkysaKzJuJOA==",
"User-Agent": "Mozilla 5.0 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H); com.google.android.gms/200616022; FastParser/1.1; ApiaryHttpClient/1.0; (gzip) (G011A N2G48H); gzip",
"content-length": "244",
"Host": "securetoken.googleapis.com",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip"}
def gas(reftoken):
	try:
		datatk = {"refresh_token":reftoken,"grant_type":"refresh_token"}
		datatk = json.dumps(datatk)
		mbl2 = {"data": {"platform": "Android","bundleid": "com.bling.bitcoinblocks"}}
		datablock = json.dumps(mbl2)
		mb11 = {"data":{"platform":"Android","bundleid":"app.getloaded.bitcoinblast"}}
		datablast = json.dumps(mb11)
		mb13 = {"data":{"platform":"Android","bundleid":"com.playday.bitcoinsolitaire"}}
		datasolid = json.dumps(mb13)
		a = r.post(gtoken,headers=hd,data=datatk).text
		b = json.loads(a)["access_token"]
		c = json.loads(a)["user_id"]
		cx = {'id_token':b}
		d = json.dumps(cx)
		e = r.post(acc,headers={'User-Agent': 'Mozilla 5.0 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H); com.google.android.gms/200616022; FastParser/1.1; ApiaryHttpClient/1.0; (gzip) (G011A N2G48H); gzip','Content-Type': 'application/json','X-Firebase-Locale': '','X-Client-Version': 'Android/GmsCore/X19002000/FirebaseCore-Android','Accept-Language': 'en-US','X-Android-Package': 'app.getloaded.bitcoinblast','X-Android-Cert': 'E998BC4F040DCA2383FAEB36E3FE5A629C31B790','X-Goog-Spatula': 'CjoKGmFwcC5nZXRsb2FkZWQuYml0Y29pbmJsYXN0Ghw2Wmk4VHdRTnlpT0QrdXMyNC81YVlwd3h0NUE9GKvkysaKzJuJOA==','content-length': '927','Host': 'www.googleapis.com','Connection': 'Keep-Alive','Accept-Encoding': 'gzip'},data=d).text
		d = json.loads(e)
		print(f'{putih}Akun ingkang nduweni email: {hijau}',d["users"][0]["email"])
		while True:
			try:
				r.post(bl2,data=datablock,headers={"Host": "us-central1-loaded-93189.cloudfunctions.net","accept": "*/*","authorization": "Bearer "+b,"content-type": "application/json; charset=utf-8","user-agent": "okhttp/3.12.1","content-length": "68"})
				j = r.post(bl1,data=datablock,headers={"Host": "us-central1-loaded-93189.cloudfunctions.net","accept": "*/*","authorization": "Bearer "+b,"content-type": "application/json; charset=utf-8","user-agent": "okhttp/3.12.1","content-length": "68"}).text
				k = json.loads(j)["result"]
				if k["message"] == "Maximum loyalty points have been earned. Come back tomorrow to continue earning loyalty points.":
					while True:
						r.post(bl2,data=datablast,headers={"Host": "us-central1-loaded-93189.cloudfunctions.net","authorization": "Bearer "+b,"content-type": "application/json; charset=utf-8","content-length": "71","accept-encoding": "gzip","user-agent": "okhttp/3.12.1"})
						l = r.post(bl1,data=datablast,headers={"Host": "us-central1-loaded-93189.cloudfunctions.net","authorization": "Bearer "+b,"content-type": "application/json; charset=utf-8","content-length": "71","accept-encoding": "gzip","user-agent": "okhttp/3.12.1"}).text
						m = json.loads(l)["result"]
						if m["message"] == "Maximum loyalty points have been earned. Come back tomorrow to continue earning loyalty points.":
							print(f"{cyan}Sampun mencapai wates amengan")
							d = r.get("https://loaded-93189.firebaseio.com/users/"+c+".json?print=pretty&auth="+b,headers={"Host": "loaded-93189.firebaseio.com","Accept": "*/*","User-Agent": "Firebase/5/19.2.1/25/Android"}).text
							print(f"{biru}wilangan loyalty poin panjenengan:{kuning}",json.loads(d)["loyaltyPointsCount"])
							break
						else:
							print(hijau+m["message"],f"{kuning}[Bitcoin Blast]")
							tunggu(random.randint(30,60))
					break
				else:
					print(hijau+k["message"],f"{kuning}[Bitcoin Blocks]")
					tunggu(random.randint(30,60))
			except Exception as e:
				print(e)
				continue
	except requests.exceptions.ConnectionError:
		print("Sesambungan Pedot..!!")
if os.name == 'nt':os.system('cls')
else:os.system('clear')

print(f"""{putih}
    _   __                  _ ______           __  
   / | / /___ _____  ____  (_)_  __/______  __/ /__
  /  |/ / __ `/ __ \/ __ \/ / / / / ___/ / / / //_/
 / /|  / /_/ / /_/ / /_/ / / / / / /  / /_/ / ,<   
/_/ |_/\__, /\____/ .___/_/ /_/ /_/   \__,_/_/|_|  
      /____/     /_/                               

{hijau}Dipunngasta dening {putih}NgopiTruk
{cyan}Matur sembah nuwun dhateng sedaya member NgopiTruk
{kuning}Dolanan Aplikasi Bling{putih}
""")

try:
	z = 1
	a = open('akun.txt').readlines()
	if len(a) == 0:
		print("mboten woonten akun kang dimainake")
		exit()
	else:
		print(f"{hijau}Jumlah akun:{putih}",len(a))
		print(" ")
		for b in a:
				bb = b.strip('\n')
				gas(bb)
				z += 1
except IOError:
	print(f"{merah}File akun.txt mboten wonten")
	exit()