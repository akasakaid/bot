import requests
from fake_useragent import UserAgent

ua = UserAgent()
link = input('>< input link pendaftaran : ')
kode = input(">< input kode referral : ")
pw = input(">> Masukkan Password untuk akun : ")


while True:
	r = requests.Session()
	headers = {
	"user-agent":ua.random
}
	r.get(link,headers=headers)
	nope = input('<> contoh : 823240232555\n>< masukkan nomor : ')
	data = {"type":"1","mobile":nope}
	a = r.post('https://imangool.com/index.php/Api/Public/smsCode',headers=headers,data=data).json()
	if a['info'] != "SUCCESS":exit("<x> Ulangi Pendaftaran Nanti!!")
	print('>< Status pengiriman OTP :',a['info'])
	otp = input('<> masukkan OTP : ')
	data = {"username":nope,"password":pw,"confirm_password":pw,"verify_code":otp,"invitation_code":kode}
	b = r.post('https://imangool.com/index.php/Api/Public/register',headers=headers,data=data).json()
	print(">< Status :",b['info'])
	ulangi = input("ulangi ? [ yes/no ]").lower()
	if ulangi == "yes":
		continue
	elif ulangi == "no":
		break
	else:
		print("LU KEK KONTOL ASW!!");exit()