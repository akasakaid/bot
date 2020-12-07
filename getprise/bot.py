import requests,json,os

r = requests.Session()

buyer = 'https://inter12580.getpraises.com/buyer'
buyertask = 'https://inter12580.getpraises.com/buyer/task/get_list?page=0&type=0'
useradd = 'https://inter12580.getpraises.com/buyer/order/add'
orderlist = 'https://inter12580.getpraises.com/buyer/order/list?status=0&page=0'
confirm = 'https://inter12580.getpraises.com/buyer/order/confirm_content'
#auth = json.loads(open('auth.json').read())['auth']

def ngebot(auth):
	headers1 = {
"Host": "inter12580.getpraises.com",
"Connection": "keep-alive",
"Accept": "application/json, text/plain, */*",
"Authorization": auth,
"lang": "Bahasa",
"Save-Data": "on",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-N950S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
"Origin": "http://home.getpraises.com",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "http://home.getpraises.com/",
"Accept-Language": "en-US,en;q=0.9"
	}
	a = r.get(buyer,headers=headers1).json()
	username,balance = a['username'],a['balance']
	print(f"Login as {username}")
	print(f"Balance : {balance}")
	while True:
		b = r.get(buyertask,headers=headers1).json()
		c = r.post(useradd,headers=headers1,data={"task_id": b[0]['id']}).json()
		if c['msg'] == 'Tugas Anda hari ini telah dikumpulkan!':
			print('Tugas Anda hari ini telah dikumpulkan!')
			break
		else:
			d = r.get(orderlist,headers=headers1).json()
			e = r.post(confirm,headers=headers1,data={'id':d[0]['id'],'img':'http://inter12580.getpraises.com/upload/160407540228612615.png'}).json()
			print(e['msg'])

os.system('cls' if os.name == 'nt' else 'clear')
ls = open('akun.txt').read().splitlines()
for xx in ls:
	print('~ '*30)
	ngebot(xx)