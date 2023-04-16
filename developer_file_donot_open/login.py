import os,subprocess,uuid, string
import random,time
try:
    import requests
except:
    os.system('pip install requests')

def login1(iid, pas):
    brands = ['Samsung', 'Oppo', 'Vivo', 'Tecno', 'Infinix']
    android = random.choice(brands)
    version = str(random.randrange(5, 11))
    fbav = str(random.randint(111, 999)) + '.' + '0' + '.' + '0' + '.' + str(random.randint(2, 9)) + '.' + str(
        random.randint(111, 999))
    fbaav = str(random.randint(10, 90)) + '.' + '1' + '.' + 'A' + '.' + '0' + '.' + str(random.randint(111, 999))
    try:
        model = subprocess.check_output('wmic csproduct get name', shell=True).decode('utf-8').strip().split('\n')[1]
    except:
        model = "Infinix Hot10"

    uas = "SupportsFresco=1 modular=1 Dalvik/2.1.0 (Linux; U; Android " + version + ".1.1; " + model + " Build/" + fbaav + ") [FBAN/FB4A;FBAV/" + fbav + ";FBBV/20748051;FBDM/{density=1.5,width=540,height=960};FBLC/nl_NL;FBCR/vodafone NL;FBMF/" + android + ";FBBD/" + android + ";FBPN/com.facebook.katana;FBDV/" + model + ";FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
    head = {'User-Agent': uas, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close',
            'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(2e4, 4e4)), 'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
    data = "adid=" + str(uuid.uuid4()) + "&format=json&device_id=" + str(uuid.uuid4()) + "&email=" + iid + "&password=" + pas + "&generate_analytics_claims=1&community_id=&cpl=true&try_num=1&family_device_id=" + str(uuid.uuid4()) + "&credentials_type=password&source=login&error_detail_type=button_with_disabled&enroll_misauth=false&generate_session_cookies=1&generate_machine_id=1&currently_logged_in_userid=0&locale=en_PK&client_country_code=PK&fb_api_req_friendly_name=authenticate&api_key=62f8ce9f74b12f84c123cc23437a4a32&access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
    checker(requests.post("https://b-graph.facebook.com/auth/login", headers=head, data=data).json())

def login2(iid, pas):
    head = {'User-Agent': '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(
        random.randint(1000, 5000)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/' + str(
        random.randint(11, 99)) + '.0.0.' + str(random.randint(1000, 5000)) + ';FBBV/' + str(random.randint(1111111,
                                                                                                            9999999)) + ';FBDM/{density=1.0,width=1024,height=552};FBLC/fr_FR;FBCR/;FBMF/archos;FBBD/archos;FBPN/com.facebook.katana;FBDV/Archos 101c Neon;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]',
            'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '329'}
    data = "adid=" + str(''.join(random.Random().choices(string.hexdigits, k=16))) + "&format=json&device_id=" + str(
        uuid.uuid4()) + "&email=" + iid + "&password=" + pas + "&generate_analytics_claims=1&credentials_type=password&source=login&error_detail_type=button_with_disabled&enroll_misauth=false&generate_session_cookies=1&generate_machine_id=1&fb_api_req_friendly_name=authenticate"
    checker(requests.post("https://b-graph.facebook.com/auth/login", headers=head, data=data).json())
def checker(po):
    if 'session_key' in po:
        open('developer_file_donot_open/.token.txt','a').write(po["access_token"])
        print(' \033[1;32mSucessfully login done ;-X \033[0m')
        time.sleep(2)
        print(f' Access Token : \033[1;36m{po["access_token"]}\033[0m')
        time.sleep(1)
        return po['access_token']
    elif 'User must verify their account on www.facebook.com' in po['error']['message']:
        print(' \033[1;31m Facebook Account Is In Checkpoint\033[0m')
        print(f' Login Another Account')
        exit()
    else:
        print(' \033[1;35m SomeThing Went Wrong Maybe Email Or Password Is Wrong\033[0m')
        print(f' Login Another Account')
        exit()
