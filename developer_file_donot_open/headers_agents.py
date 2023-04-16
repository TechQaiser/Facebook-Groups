import random

NAME_DEVICES = [["Samsung", "Galaxy S21 Ultra", "RP1A.200720.012", "11"],
                ["Google", "Pixel 6", "RD2A.210305.006", "12"],["OnePlus", "9 Pro", "11.2.8.8.LE15AA", "11"],
                ["Xiaomi", "Redmi Note 10 Pro", "RKQ1.200826.002", "11"],["Motorola", "Moto G Power", "QPTS30.80-111-3-11", "11"],
                ["Nokia", "7.2", "00WW_4_15A", "10"],["LG", "V60 ThinQ 5G", "QKQ1.200504.002", "10"],["Sony", "Xperia 5 II", "58.1.A.5.159", "10"],["Asus", "ZenFone 7 Pro", "WW_29.13.7.47", "11"],["HTC", "U12+", "3.37.617.18", "9"],["ZTE", "Axon 10 Pro", "A2020RU1.0.0B10", "10"],
                ["Lenovo", "Legion Phone Duel", "L78051_ROW_OPS_1.45.ROW", "10"],["Realme", "GT Neo2", "RMX3271_11_A.06", "11"],
                ["Oppo", "Find X3 Pro", "CPH2173_11_F.10", "11"],["Vivo", "iQOO 7 Legend", "PD1981F_EX_A_6.2.18", "11"],["Poco", "X3 NFC", "V12.0.4.0.RJGMIXM", "11"],["BlackBerry", "Key2", "ABD148", "8.1"],["Sharp", "Aquos R5G", "SGX002N_00WW", "10"],["TCL", "10 Pro", "T799B07", "10"],["Honor", "Magic 3", "ELS-TN00_11.0.0.183", "11"],["Redmi", "Note 8 Pro", "QCOM_19304_11.0.3", "11"],["Infinix", "Hot 10T", "X690B-H6216JQK-P-210222V326", "11"],["Oukitel", "WP10", "WP10_V1.0_20210522", "10"],["Doogee", "S96 Pro", "DOOGEE_S96_Pro_EEA_20210302", "10"],["Tecno", "Camon 17 Pro", "CE9-H693AD-Q-GL-200730V278", "11"],["Ulefone", "Armor 11 5G", "ULEFONE_ARMOR_11_5G_V1.1_20210408", "11"],["Cubot", "KingKong 5 Pro", "CUBOT_KINGKONG5PRO_20210811", "11"],["Cat", "S62 Pro", "CS62PRO_20210416_V3", "10"]]

def useragent() -> str:
    randomly_chooser = random.choice(NAME_DEVICES)
    android, model, build, version = randomly_chooser[0], randomly_chooser[1], randomly_chooser[2], randomly_chooser[3]
    fbav, fbbv = random.choice(
        ['369.0.0.18.103-373751439', '321.0.0.28.120-388307802', '326.0.0.48.116-388473031', '324.0.0.48.154-377743087',
         '319.0.0.45.119-388854492', '303.0.0.39.192-384235218']).split('-')
    networks = 'Jazz', 'Zong', 'AT&amp', '02'
    carrier = random.choice(networks)
    dhw = "{density=2.25,width=720,height=1452}"
    return f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{dhw};FBLC/en_US;FBRV/0;FBCR/{carrier};FBMF/{android} MOBILE LIMITED;FBBD/{android};FBPN/com.facebook.katana;FBDV/{model};FBSV/{version};FBOP/1;FBCA/arm64-v8a:;]"

def headers1():
    token = open('developer_file_donot_open/.token.txt', 'r').read()
    headers = {
        "Host": "graph.facebook.com",
        "Priority": "u=3, i",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Graphql-Client-Library": "graphservice",
        "X-Fb-Search-Serp": "1",
        "X-Fb-Connection-Subtype": "none",
        "X-Fb-Privacy-Context": "c0000000596b1044",
        "X-Fb-Background-State": "1",
        "User-Agent": useragent(),
        "X-Fb-Net-Hni": "41001",
        "X-Fb-Sim-Hni": "41001",
        "Authorization": f"OAuth {token}",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Device-Group": "265",
        "X-Tigon-Is-Retry": "False",
        "X-Fb-Friendly-Name": "SearchResultsGraphQL",
        "X-Fb-Request-Analytics-Tags": "graphservice",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Server-Cluster": "True",
        "Content-Length": "3606"
}
    return headers

def headers2():
    ip = str(random.randint(100,299))
    headers: dict = {
        'Host': 'web.facebook.com',
        'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+ip+'.0.'+str(random.randint(555,599))+'.'+ip+' Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close'
    }
    return headers
