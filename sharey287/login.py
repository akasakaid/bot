import requests,json,time,os,click

r = requests.Session()

url_login = 'http://www.sharey287.com/api/User/Login'
gettasklist = 'http://www.sharey287.com/api/task/getTaskList'
url_rec_task = 'http://www.sharey287.com/api/task/receiveTask'
url_order_list = 'http://www.sharey287.com/api/task/taskOrderlist'
url_submit = 'http://www.sharey287.com/api/task/taskOrderSubmit'
headers = {
"Accept": "application/json, text/plain, */*",
"Accept-Language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
"Host": "www.sharey287.com",
"Origin": "http://www.sharey287.com",
"Referer": "http://www.sharey287.com/",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36",
}

def login(username,password):
	data = {"username":username,"password":password,"lang":"id"}
	a = r.post(url_login,headers=headers,data=data).json()
	if a['code'] != 1:
		print(a['code_dec'])
	else:
		status = a['code_dec']
		token = a['info']['token']
		uid = a['info']['uid']
		username = a['info']['username']
		ip = a['info']['ip']
		balance = a['info']['balance']
		tingkat = a['info']['useridentity']
		print(f"""{status} | {ip}
Username : {username} | Balance : {balance} | Tingkat : {tingkat}""")
		for x in range(5):
			print('- '*25)
			b = r.post(gettasklist,headers=headers,data={"group_id": "42","task_level": "1","page_no": "1","is_u": "0","lang": "id","token": token}).json()
			task_id = b['info'][0]['task_id']
			c = r.post(url_rec_task,headers=headers,data={'id':task_id,"lang":"id","token":token}).json()
			print(f"Menerima tugas",c['code_dec'])
			if c['code_dec'] == 'gagal':break
			d = r.post(url_order_list,headers=headers,data={"status": "1","page_no": "1","is_u": "2","lang": "id","token": token}).json()
			if d['code'] == 0:print('Tidak Ada Tugas !')
			else:
				order_id = d['info'][0]['order_id']
				reward = d['info'][0]['reward_price']
				print(f"Order ID : {order_id} | Reward : {reward}")
				e = r.post(url_submit,headers=headers,data={"order_id": order_id,"examine_demo[]": "/upload/image/20201102/77a766eca18ba54b98f88e994a3b0a1b.jpeg","lang": "id","token": token}).json()
				print(f"Submit Tugas",e['code_dec'])

os.system('cls' if os.name == 'nt' else 'clear')
ls = open('akun.txt').read().splitlines()
for xx in ls:
	print('*'*50)
	nomor = xx.split(' ')[0]
	pw = xx.split(' ')[1]
	login(nomor,pw)
print('*'*50)