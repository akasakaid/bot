#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    from telethon import TelegramClient, sync, events
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
    from telethon.errors import SessionPasswordNeededError as __butuhpw__
    from colorama import Fore as __fore__
    from colorama import init as __nit__
    import time,os,sys,re,requests
except ImportError:exit('please install module !! \n pip3 install -r requiremensts.txt')
__nit__(autoreset=True)
__merah__ = __fore__.LIGHTRED_EX
__kuning__ = __fore__.LIGHTYELLOW_EX
__hijau__ = __fore__.LIGHTGREEN_EX
__biru__ = __fore__.LIGHTBLUE_EX
__magenta__ = __fore__.LIGHTMAGENTA_EX
__cyan__ = __fore__.LIGHTCYAN_EX
__hitam__ = __fore__.LIGHTBLACK_EX
__putih__ = __fore__.LIGHTWHITE_EX
__reset__ = __fore__.RESET
__r__ = requests.Session()
def __tunggu__(__t__):
    while __t__:
        print(f' {__hijau__}[{__cyan__}●         {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●        {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●       {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●      {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●●     {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●●●    {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●●●●   {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●●●●●  {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●●●●●● {__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        print(f' {__hijau__}[{__cyan__}●●●●●●●●●●{__hijau__}]{__putih__} {__t__} {__hijau__}s ',flush=True,end='\r')
        time.sleep(0.1)
        __t__ -= 1

def __filter__(bot):
    if bot == "DOGE":
        __bot__ = "@adsgram_doge_bot"
    elif bot == "BTC":
        __bot__ = "@adsgram_btc_bot"
    elif bot == "LTC":
        __bot__ = "@adsgram_ltc_bot"
    else:exit('Bot not found !!')
    return __bot__

if len(sys.argv) < 3:
    exit()
if not os.path.exists('sesi'):os.makedirs('sesi')
if not os.path.exists('.password'):os.makedirs('.password');ope = open('.password/.pw.txt','w');ope.write('AkasakaID');ope.close()
_bot_ = sys.argv[2].upper()
__bot__ = __filter__(bot=_bot_)
print(__bot__)
print(_bot_)

try:
    __aa__ = __r__.get('https://akasakaid.github.io/adsgram-ltc-bot/bener.txt').text
    __bb__ = __r__.get('https://akasakaid.github.io/adsgram-ltc-bot/info.txt').text
    with open('.password/.pw.txt') as __pw__:
        __pws__ = __pw__.read()
        if __pws__ != str(binascii.unhexlify(__aa__),'utf-8'):
            print(f'visit this link to get password : {__hijau__}{__bb__}')
            __cc__ = input(f'{__reset__}input password {__merah__}:{__biru__} ')
            if __cc__ != str(binascii.unhexlify(__aa__),'utf-8'):exit(f'{__reset__}visit this link to get password : {__hijau__}{__bb__}')
            with open('.password/.pw.txt','w') as __pw__:__pw__.write(__cc__)
        elif __pws__ == __aa__:exit('HAHA CHEATER DETECTED ')
        __client__ = TelegramClient('sesi/' + nomor, 1148490, 'd82c81323285aeb9c2ba9ee420d8b009')
        __client__.connect()
        if not __client__.is_user_authorized():
            try:
                __client__.send_code_request(nomor)
                __client__.sign_in(nomor, input('enter the code: '))
            except SessionPasswordNeededError:
                passw = input('password 2fa: ')
                __client__.start(nomor, passw)
        me = __client__.get_me()
        depan = me.first_name
        pon = nomor[0:5]
        pho = nomor.replace(pon,'****')
        bot_username = '@adsgram_ltc_bot'
        bot_entity = __client__.get_entity('@adsgram_ltc_bot')
        print(f'{kuning}user information')
        print(f'{hijau}first name {merah}:{putih} {depan}')
        print(f'{hijau}phone {merah}: {putih}{pho}')
        print(' ')
        print(f'{putih}[{hijau}*{putih}] {hijau}starting bot !!')
        while True:
            try:
                __client__.send_message(bot_username,message="💻 Visit Sites")
                print(f'{putih}[{kuning}!{putih}] {kuning}getting url                           ',flush=True,end='\r')
                time.sleep(3)
                rw = __client__(GetHistoryRequest(peer=bot_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                id = rw.messages[0].id
                if 'There are no new Task available for you' in rw.messages[0].message :
                    print(f'{putih}[{merah}x{putih}] {merah}There are no new Task available for you !!{reset}')
                    __client__.send_message(bot_username,message="💰 Balance")
                    time.sleep(2)
                    rw = __client__(GetHistoryRequest(peer=bot_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    bl = re.search(r'(.*) LTC',rw.messages[0].message).group(1)
                    bl = bl.strip()
                    exit(f'{putih}[{hijau}+{putih}] {hijau}balance {merah}:{putih} {bl}')
                url = rw.messages[0].reply_markup.rows[0].buttons[0].url
                urpar = urllib.parse.unquote(url)
                idv = urpar.replace('http://adsgram.co/ltc/visit/','')
                r1 = r.post('http://adsgram.co/ltc/assets/ajax/iframe.php',headers=headers,data={'a':'v','ad':idv})
                tm = re.search(r'"(.*)"',r1.text).group(1)
                tunggu(int(tm))
                r2 = r.post('http://adsgram.co/ltc/assets/ajax/iframe.php',headers=headers,data={'a':'c','ad':idv})
                time.sleep(2)
                rw = __client__(GetHistoryRequest(peer=bot_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                rew = re.search(r'earned (.*) LTC',rw.messages[1].message).group(1)
                print(f'{putih}[{hijau}+{putih}] {hijau}you earned {rew} LTC for visiting a site !!')
            except ValueError:
                __client__(GetBotCallbackAnswerRequest(bot_username,id,data=rw.messages[0].reply_markup.rows[1].buttons[1].data))
                time.sleep(2)
                print(f'{putih}[{merah}x{putih}]{merah}                                      skipping ads');continue
            except telethon.errors.rpcerrorlist.TimeoutError:continue
