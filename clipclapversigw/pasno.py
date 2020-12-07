from colorama import *
init(autoreset=True)
merah = Fore.LIGHTRED_EX
kuning = Fore.LIGHTYELLOW_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
hitam = Fore.LIGHTBLACK_EX
putih = Fore.LIGHTWHITE_EX
reset = Fore.RESET
import time
def wk(t):
    while t:
        print(f'[●         ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●        ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●       ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●      ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●     ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●    ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●   ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●●  ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●●● ] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f'[●●●●●●●●●●] {t} s ',flush=True,end='\r')
        time.sleep(0.1)
        t -= 1

wk(300)