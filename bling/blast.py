from datetime import datetime
from pytz import timezone
import requests,json,time,os,random,re
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

def banner():
    os.system('cls' if os.name == 'nt' else 'cls')
    print("""    ____  ___            
   / __ )/ (_)___  ____ _
  / __  / / / __ \/ __ `/
 / /_/ / / / / / / /_/ / 
/_____/_/_/_/ /_/\__, /  
                /____/   
Black Coder Crush
- Bitcoin Blast
    """)

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
    "Accept-Encoding": "gzip"
    }

def sig():
    headers = {
    'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,mt;q=0.7',
    'cache-control': 'no-cache',
    'content-length': '114',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_gp_time_zone=Asia/Jakarta; _ga=GA1.2.1658849966.1589674733; _gid=GA1.2.370866484.1589674733; __gads=ID=a1f56866de1722b1:T=1589674770:S=ALNI_MaXtX2HKaDOhGAKlTObwk2dCb1ysw; _gp_session=OWJlcUJGK3p6cHFac2EwUGhna2dWeXpOYUYrTE1TLzNXcHh3Mjd2QU9STzdoTDZmaW1va1orb3haMlJ6eTVVb1ZTT0tVaWg5WkpRZmREMisyMFRVTVh5ZHBNeHJweEM2a2NwSDlJY09IVkV1MkJscXpKclN0TWpjMnM2UUM2MW1yK3g1NFRaMGNuYXZjN2NEUjlUN01qc25aY01BK2NGS3hOcjJvWGlIWjJjTHlQSE16Y3JTZm53bm95alRldGZoem53aWN4ZTc1TzJsWHNFSENicDhKVWhQZ2hORngyUW1vbXVDWUZjWjFDYkYwS0RjQVhqbTZKcEd0VkF2dEsvVS0tRVJHWEFjZ09ucmhlZm5lak0vVWRidz09--3274959436f1d698e9c4f58b31fc23dbdd300bc5',
    'origin': 'https://generate.plus',
    'pragma': 'no-cache',
    'referer': 'https://generate.plus/en/base64',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'x-csrf-token': 'NAAiwC/iDbZ7v8OGFQKT0ytckCoVHLgT/efh3nrKmqXmUJE6gU+zkWxVXGSOATkFkP1RbC4s+9Qt8mV0GoRGpQ==',
    'x-requested-with': 'XMLHttpRequest'
    }
    data = {
    'utf8': '✓',
    'gp_base64_base[card]': 'single',
    'gp_base64_base[length]': 20,
    'gp_base64_base[urlsafe]': 0,
    'button': ''}
    a = r.post('https://generate.plus/en/base64',data=data,headers=headers)
    b = re.search('<li>(.*?)</li>',a.text).group(1)
    return b


def gas(reftoken):
    try:
        datatk = json.dumps({"refresh_token":reftoken,"grant_type":"refresh_token"})
        a = r.post(gtoken,headers=hd,data=datatk).text
        b = json.loads(a)["access_token"]
        c = json.loads(a)["user_id"]
        cx = {'id_token':b}
        d = json.dumps(cx)
        e = r.post(acc,headers={
            'User-Agent': 'Mozilla 5.0 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H); com.google.android.gms/200616022; FastParser/1.1; ApiaryHttpClient/1.0; (gzip) (G011A N2G48H); gzip',
            'Content-Type': 'application/json',
            'X-Firebase-Locale': '',
            'X-Client-Version': 'Android/GmsCore/X19002000/FirebaseCore-Android',
            'Accept-Language': 'en-US',
            'X-Android-Package': 'app.getloaded.bitcoinblast',
            'X-Android-Cert': 'E998BC4F040DCA2383FAEB36E3FE5A629C31B790',
            'X-Goog-Spatula': 'CjoKGmFwcC5nZXRsb2FkZWQuYml0Y29pbmJsYXN0Ghw2Wmk4VHdRTnlpT0QrdXMyNC81YVlwd3h0NUE9GKvkysaKzJuJOA==',
            'content-length': '927',
            'Host': 'www.googleapis.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
            },data=d).text
        d = json.loads(e)
        print(f'{putih}Akun {merah}: {hijau}',d["users"][0]["email"])
        while True:
            try:
                now = datetime.now(timezone('UTC'))
                stm = datetime.timestamp(now)
                sigg = sig()
                data_blast = json.dumps({"data": {"platform": "Android","advertid": "165197e1-5043-432b-8e14-a0aa5a2b7410","appdeviceguid": "0b7e3566-6df0-49a7-93ed-24a0a6f0c97e","version": "1.0.24","timezoneoffset": "7","bundleid": "com.bling.bitcoinblocks","lastuid": c,"language": "English","advertidtracking": "True","sig": sigg,"currenttimeutc": stm}})
                j = r.post(bl1,data=data_blast,headers={
                    "Host": "us-central1-loaded-93189.cloudfunctions.net",
                    "accept": "*/*",
                    "authorization": "Bearer "+b,
                    "content-type": "application/json; charset=utf-8",
                    "user-agent": "okhttp/3.12.1"
                    }).text
                k = json.loads(j)["result"]
                if k["message"] == "Maximum loyalty points have been earned. Come back tomorrow to continue earning loyalty points.":
                    print(f'{merah}Sudah mencapai limit harian !!')
                else:
                    print(hijau+k["message"],f"{kuning}[Bitcoin Blast]")
                    tunggu(random.randint(30,60))
            except Exception as e:
                continue
    except requests.exceptions.ConnectionError:
        exit(f"{merah}Lost Internet Connection !!")

banner()
try:
	a = open('akun.txt').readlines()
	if len(a) == 0:
		exit(f"{merah}Tidak ada akun !!")
	else:
		print(f"{hijau}Jumlah akun:{putih}",len(a))
		print(" ")
		for b in a:
				bb = b.strip('\n')
				gas(bb)
except IOError:
	exit(f"{merah}File akun.txt tidak ada !!")
