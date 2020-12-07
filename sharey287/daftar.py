import requests,json,time,os,click

r = requests.Session()
password = 'zonanyaman123'

def daftar(nomor,kode):
	t = int(time.time())
	code = r.get(f'http://www.sharey287.com/api/Account/code?code_rand={t}')
	open('captcha.jpg','wb').write(code.content)
	click.launch('captcha.jpg')
	cap = input('# input captcha : ')
	data = {"dest":"62","username":nomor,"password":password,"re_password":password,"smscode":"","code":cap,"code_rand":t,"recommend":kode,"lang":"id"}
	headers = {
	"Accept": "application/json, text/plain, */*",
	"Accept-Language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
	"Connection": "keep-alive",
	"Content-Type": "application/x-www-form-urlencoded",
	"Host": "www.sharey287.com",
	"Origin": "http://www.sharey287.com",
	"Referer": "http://www.sharey287.com/",
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"
	}
	a = r.post('http://www.sharey287.com/api/user/Register',headers=headers,data=data).json()
	print(a)

daftar(input("# phone number : "),"9632145")
