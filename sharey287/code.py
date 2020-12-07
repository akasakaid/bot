import requests,time

r = requests.Session()
t = time.time()
a = r.get(f'http://www.sharey287.com/api/Account/code?code_rand={t}')
open('hasil.jpg','wb').write(a.content)