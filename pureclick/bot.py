import requests,os,threading,time,sys
from bs4 import BeautifulSoup as bs

r = requests.Session()

headers_page = {
	"Host": "pureclick.xyz",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"referer": "https://pureclick.xyz/account",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

headers_faucet = {
	"Host": "pureclick.xyz",
	"origin": "https://pureclick.xyz",
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"referer": "https://pureclick.xyz/faucet",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

def faucet(cookie):
#	while True:
		try:
			a = r.get('https://pureclick.xyz/faucet',headers=headers_page,cookies={'ci_session':cookie}).text
			b = bs(a,'html.parser')
			mel = b.find('a',attrs={"class":"nav-link dropdown-toggle","data-toggle":"dropdown"}).text.strip()
			c = b.find('li',attrs={'class':'nav-item active balance'}).text.strip()
			d = b.find('input',attrs={'type':'hidden','name':'csrf_token_name'})['value']
			e = b.find('input',attrs={'name':'token','type':'hidden'})['value']
			data = {'csrf_token_name':d,'token':e}
			f = r.post('https://pureclick.xyz/faucet/verify',headers=headers_faucet,data=data,cookies={'ci_session':cookie})
			return mel,c
		except AttributeError:pass
		except requests.exceptions.ConnectionError:pass
		except TypeError:pass

ls = open(sys.argv[1]).read().splitlines()[0]
while True:
	try:
		m = faucet(ls)
		bb = int(m[1].replace(' (current)',''))
		if bb > 200:
			a  = r.get('https://pureclick.xyz/account',headers=headers_page,cookies={'ci_session':ls}).text
			b = bs(a,'html.parser')
			c = b.find('input',attrs={'type':'hidden','name':'csrf_token_name'})['value']
			data = {'csrf_token_name':c,'action':'withdraw'}
			d = r.post('https://pureclick.xyz/account/withdraw',headers=headers_faucet,cookies={'ci_session':ls},data=data)
			print(m[0],'| withdraw',bb)
			text = f"{m[0]} | withdraw {bb} litoshi"
			r.get(f'https://api.telegram.org/bot1489009706:AAG9DpI46INL5LM5I3R-1jLT97wvNF9v-mQ/sendmessage?chat_id=629438076&text={text}')
		else:
			print(m[0],'| balance',bb)
#			time.sleep(1)
	except TypeError:continue
	except KeyboardInterrupt:exit()