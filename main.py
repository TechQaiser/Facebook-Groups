import json, sys, os, time, re, uuid, datetime, codecs
try:
    import requests
except:
    os.system('pip install requests')
    import requests

from time import sleep
from os import system as stm
import platform, unicodedata
# --->>> colors
red = '\033[1;91m'
green = '\033[1;92m'
yellow = '\033[1;93m'
blue = '\033[1;94m'
pink = '\033[1;95m'
cyan = '\033[1;96m'
lred = '\033[1;31m'
lgreen = '\033[1;32m'
lyellow = '\033[1;33m'
lblue = '\033[1;34m'
lpink = '\033[1;35m'
lcyan = '\033[1;36m'
dark ='\033[31;44m'
dark2 ='\033[35;43m'
dark3 ='\033[33;5;41m'
stop = '\033[0m'
total = []

def slow_writter(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.05)

if platform.system() == 'Windows':
    c = 95
    cls = 'cls'
    banner = f"""
      {green} ██████{lcyan}╗{green} ███████{lcyan}╗{green}██████{lcyan}╗{green}     ███████{lcyan}╗{green} █████{lcyan}╗  {green}██████{lcyan}╗{green}██████{lcyan}╗  {green}██████{lcyan}╗ {green} ██████{lcyan}╗ {green}██{lcyan}╗  {green}██{lcyan}╗
      {green}██{lcyan}╔═══{green}██{lcyan}╗{green}██{lcyan}╔════╝{green}██{lcyan}╔══{green}██{lcyan}╗    {green}██{lcyan}╔════╝{green}██{lcyan}╔══{green}██{lcyan}╗{green}██{lcyan}╔════╝{green}██{lcyan}╔══{green}██{lcyan}╗{green}██{lcyan}╔═══{green}██{lcyan}╗{green}██{lcyan}═══{green} ██{lcyan}╗{green}██{lcyan}║{green} ██{lcyan}╔╝
      {green}██{lcyan}║   {green}██{lcyan}║{green}███████{lcyan}╗{green}██████{lcyan}╔╝{green}    █████{lcyan}╗{green}  ███████{lcyan}║{green}██{lcyan}║{green}     ██████{lcyan}╔╝{green}██{lcyan}║   {green}██{lcyan}║{green}██{lcyan}║   {green}██{lcyan}║{green}█████{lcyan}╔╝ 
      {green}██{lcyan}║{green}▄▄ ██{lcyan}║╚════{green}██{lcyan}║{green}██{lcyan}╔══{green}██{lcyan}╗{green}    ██{lcyan}╔══╝{green}  ██{lcyan}╔══{green}██{lcyan}║{green}██{lcyan}║     {green}██{lcyan}╔══{green}██{lcyan}╗{green}██{lcyan}║  {green} ██{lcyan}║{green}██{lcyan}║   {green}██{lcyan}║{green}██{lcyan}╔═{green}██{lcyan}╗ 
      {lcyan}╚{green}██████{lcyan}╔╝{green}███████{lcyan}║{green}██{lcyan}║{green}  ██{lcyan}║ {green}   ██{lcyan}║{green}     ██{lcyan}║{green}  ██{lcyan}║╚{green}██████{lcyan}╗{green}██████{lcyan}╔╝╚{green}██████{lcyan}╔╝╚{green}██████{lcyan}╔╝{green}██{lcyan}║{green}  ██{lcyan}╗
       {lcyan}╚══{green}▀▀{lcyan}═╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝"""
elif platform.system() == 'Android':
    c = 50
    cls = 'clear'
    banner = f"""
        {green} ██████{lcyan}╗{green} ███████{lcyan}╗{green}██████{lcyan}╗{green}
        {green}██{lcyan}╔═══{green}██{lcyan}╗{green}██{lcyan}╔════╝{green}██{lcyan}╔══{green}██{lcyan}╗
        {green}██{lcyan}║   {green}██{lcyan}║{green}███████{lcyan}╗{green}██████{lcyan}╔╝ 
        {green}██{lcyan}║{green}▄▄ ██{lcyan}║╚════{green}██{lcyan}║{green}██{lcyan}╔══{green}██{lcyan}╗ 
        {lcyan}╚{green}██████{lcyan}╔╝{green}███████{lcyan}║{green}██{lcyan}║{green}  ██{lcyan}║
        {lcyan}╚══{green}▀▀{lcyan}═╝ ╚══════╝╚═╝  ╚═╝"""

# --->>> logo
logo = f"""
{banner}
{c * '-'}
          -> Tool Is Developed by : Qsr
          -> Youtube Channel Name : Tech Qsr
          -> Contact : Github -->> @TechQaiser 
{c * '-'}{stop}"""

def end_result(file):
    print(c * f'{lcyan}-{stop}')
    print(f'{lyellow} Process Sucessfully Completed {stop}')
    print(f'{lcyan} Total Groups Done {stop}{lgreen}{len(total)}{stop}')
    print(f'{lcyan} File Saved In {stop}{lgreen}{file}{stop}')
    print(c * f'{lcyan}-{stop}')
    input("Press Enter To Go Back ! ")
    main_dashboard()


def main_dashboard():
    stm(cls)
    print(logo)
    print(f" {yellow}[{cyan}1{stop}{yellow}]. {green}Extract groups by names, keywords {dark}  (Most Demand)  {stop}")
    print(f" {yellow}[{cyan}2{stop}{yellow}]. {green}Extract groups by other groups ids {dark2}  (Unlimmited Groups)  {stop}")
    print(f" {yellow}[{cyan}3{stop}{yellow}]. {green}Extract groups by names with countries {dark}  (Filter Country)  {stop}")
    print(f" {yellow}[{cyan}4{stop}{yellow}]. {green}Extract highly pure active group {dark3}     No-Need-Login    {stop}")
    print(f" {yellow}[{cyan}5{stop}{yellow}]. {green}Extract auto approvals group {dark3}     No-Need-Login    {stop}")
    print(f" {yellow}[{lred}R{stop}{yellow}]. {green}Remove Old Login facebook account Add New")
    print(f" {pink}[0]. Exit Tool Go Back{stop}")
    print(c * f'{lcyan}-{stop}')
    parser = input(' Select Option To Use -> ')
    if parser in ['1', '01']:
        login();main().groups_by_names_keywords()
    if parser in ['2', '02']:
        login();main().group_by_id()
    if parser in ['3', '03']:
        login();main().group_by_country()
    if parser in ['4', '04']:
        main_nologin().extract_pure_active()
    if parser in ['5', '05']:
        main_nologin().extract_auto_approval()
    else:
        exit(' invalid menu choosen !')

class login():
    def __init__(self):
        stm(cls)
        print(logo)
        try:
            token_file = 'developer_file_donot_open/.token.txt'
            self.token = open(token_file, 'r').read()
            otw = requests.get('https://graph.facebook.com/me?access_token=' + self.token)
            a = json.loads(otw.text)
            try:
                name = a['name']
                # print(f" {cyan}         Welcome Brother : {lpink}[{name}]{stop}")
                # time.sleep(2)
                # print(90 * f'{lcyan}-{stop}')
            except Exception as c:
                os.remove(token_file)
                print(f" Login Again ! \n {c}")
                time.sleep(1)
                stm(cls)
                print(logo)
                self.login_me()
        except FileNotFoundError:
            self.login_me()
    def login_me(self):
        print(f' {lpink} Login Account ! Select Any One Method From Here')
        print(c * f'{lcyan}-{stop}')
        print(f" {yellow}[{cyan}1{stop}{yellow}]. {green}Login Account Using Facebook Method ")
        print(f" {yellow}[{lred}2{stop}{yellow}]. {green}Login Account Using Facebook Lite Method{stop}")
        print(c * f'{lcyan}-{stop}')
        parser = input(' Select Option To Login -> ')
        from developer_file_donot_open import login as login_kar
        if parser in ['1', '01']:
            stm(cls)
            print(logo)
            login_kar.login1(input(' Email : '),input(' Pasword : '))
            stm(cls)
            print(logo)
        elif parser in ['2', '02']:
            stm(cls)
            print(logo)
            login_kar.login2(input(' Email : '),input(' Pasword : '))
            stm(cls)
            print(logo)

class main():
    def __init__(self):
        stm(cls)
        print(logo)
        from developer_file_donot_open import headers_agents
        token_file = 'developer_file_donot_open/.token.txt'
        self.token = open(token_file, 'r').read()
        self.page1 = 'AbpzrKcXajr_FYRZ2uLB4wTguP7HHQaRTuIufuuoIsshT_Pli4xZmMxDleMqmNCpN9BAcR43bEMs-QEfXYSoStlH6jaIZzS2zzVB98DBW0Eg1iMUMw76lfBZUzPH6pKaYym4MIIsIs-IoFajKzKaF264-k0Kb99YmVdHnQlj4SSHhOo-VkP1ovP7ap8BFgLhfMKmeCS4-N1vl5-zy2IAi2gnbBpMmRlOmwi43_811mb4RSbmhG2r763ru-UCOKQrVZBFwG8IOWCF3pJXH26d2V8ETgE6LC1TvS1dG-aIVOrffq0OAnIVSssbGZaJ1hsqTd_bPB-7Vn-Da17SWWEimWwflJZxCx8ylEayQ4kgrqqdlDJZihia7Jtgz_jjYFwKQLld3AHlCsaqt6o7apNQ7OKHC-Rnv9s5Gn-EllGApqCWWgXpQ03bH9oGMOITM7nSbctc-kxebtlEGji2cSVPc82bz2AVLrTuqWWCzya5-XCM_w6-RnfdKg2i1CRaO9eY9KEOFbdeb07uZloUxHZ1QmmWE-ADnVv7LGMK77yTRQ0ME4WgTZAFj6VDtm_dV85XqTkJiCEd0ciwX3YnH_iEnwcaxStzpGL9Y1huXHPRM6yNo0EJSflmZtrIV_RW3pd-LbBb0j1RTc08uMGeGLbnUJcAV4PD7c1ms5u8ExsdRzfGndWFra62HHJScyMamnQUbSFpzo2i7eHIyN3j4QwxHEKHGcMM_0LcUZhr5vsKinXN-58nZWTiqbWDPY1uRCNAyX4X0QKrvxINc3FgGqQcfrocBXUNX0W-WPE1M2em31me3sbwp5ON0GXH0PJe6P6ZHCvIOkUBhY91HFqwRE414t0Dl_Spdu2sJJT3yMTEfMAcFCc00OCY7eOeh-yoJqeIdn38N-RhOOAM0UNkLCjbrBPo5HhLLzwP986j-xwQjVzcC7XKCb83Gk5uXR7AhAL8u2lerWQ5YhCqjBH6q6TBOHxVeOuwtdCBao-YvC3wnljOpWOlobNQvLi7tf3MOhpVYVJwWbiRrNJz-70oBGS_3Ee0Lfr1jRRI3V-vPyCfF3MSxco6lxZOPBzLDYzYPxecqsk6Yp5RUDoOmzo21jbsdFYr5-ZOe8J3CZ_R8ySgHjQLc5o2svFIfe7QlUH0ygQfIckrrW3x2scv7Z763hcUr5vPtku65VLR3nSnVphSCWQoLhZNs0GFrVfyy4Siy68YuEveVckzH-RSbCSQXEKZA3824h-Kj4lgSeHJBZ-34yKb62ehLGpjbA52dBgBDeyvUYZmdqvAD1L_1iWfwQZnKQUQKUUay-bIJdcgNJrJTSjRrm-cogfgs7sJpOPM5NKFVnoI3cTWWzGTpbwwcATbFxLyQoPegw3yhxErWZDV8wAe2V7775VdAc1cBnl68kS5e88N9guhozW7CDpTqSsyndgJRncT3BlJ8L0LSLzTt8SgW8QNetNtKeSQpLXp2_fUvG1DWtn9URvayws_7uN489db-5FGm1iO-BQBlDEXfOxIljrEN4DtDQEQ6Rr1f1rWhJRk3ohkrhF30a4GYEEgEQPjv9hcZLQx4aeGSi3SzUNZENZ67ASzJfwWtiOjpb3BZbYCVp0uil-1dY2ZALFXFfor6jlkbRVGPqI4Ez-8V0KChUnpk39vlqoUuGa6Sps7EkXiAB8-1K5xctBns__Mj_aQ7wubq24D0VbS9-wBQtsyEI09hUFWn4Eo6t1qpQcvO0qT8qfcB0tKiwOtAh60rtVVufBhoP8a6JWLCsZOSGC0XUn14k-9QoSt3sBlT2elGFNlSm6bvGJ0tjhlwUMXunZc5msuLBUxj4V1seJLv6h3kTQAgOzeFi--8y_AwLCY6E4uUOZe6vMwPAb56cGjE7Q9LSfXUHD5y4vvZksBqIEL0nQRQ9H8Se0geRZlJ3Ed9zs'
        self.file = open('input_data.txt', 'r').readlines()
        self.headers = headers_agents.headers1()
        self.headers2 = headers_agents.headers2()
        self.filenm = datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
        self.namefile = open(f'data/{self.filenm}.txt','a',encoding='utf-8')
    def data_http(self, groups_name):
            data = {
                "client_doc_id": "395907910716176498299001478287",
                "method": "post",
                "locale": "en_US",
                "pretty": "false",
                "format": "json",
                "variables": '{"default_image_scale":3,"nt_context":{"using_white_navbar":true,"pixel_ratio":3,"styles_id":"c86e2eaa6c16a4f0fa7d2a955a7a8004","bloks_version":"f7474c5acff3b37762d44692791f804159a49cf699021ba3623bcb76ea1576a2"},"bsid":"' + str(uuid.uuid4()) + '","entered_query_text":"","image_low_width":240,"disable_story_menu_actions":false,"query_source":"unknown","ui_theme_name":"","end_cursor":"' + self.page1 + '","supported_experiences":["FAST_FILTERS","FILTERS","FILTERS_AS_SEE_MORE","INSTANT_FILTERS","MARKETPLACE_ON_GLOBAL","MIXED_MEDIA","NATIVE_TEMPLATES","NT_ENABLED_FOR_TAB","NT_SPLIT_VIEWS","PHOTO_STREAM_VIEWER","SEARCH_SNIPPETS_ICONS_ENABLED","USAGE_COLOR_SERP","commerce_groups_search","keyword_only"],"image_large_aspect_width":720,"image_high_width":720,"inline_comments_location":"search","callsite":"android:group_search","image_large_aspect_height":376,"image_medium_width":360,"product_item_image_size":342,"profile_image_size":212,"scale":"3","bqf":"keywords_groups(' + groups_name + ')","tsid":"' + str(uuid.uuid4()) + '","request_index":0}',
                "fb_api_req_friendly_name": "SearchResultsGraphQL",
                "fb_api_caller_class": "graphservice",
                "fb_api_analytics_tags": '["pagination_query","GraphServices"]',
                "server_timestamps": "true"
            }
            try:
                po = requests.post('https://graph.facebook.com/graphql?', headers=self.headers, data=data).text
                if 'Rate limit exceeded' in po:
                    slow_writter(' You are restricted from facebook for sometime with this facebook account try after some hours or login other id ')
                    exit()
                else:
                    return po
            except requests.exceptions.ConnectionError:
                text = f'{red} Your network is slow due to that tool also work slow {stop}'
                print(text)
                time.sleep(7)
                return text
    def groups_by_names_keywords(self):
        print(f' {lpink} For Multiple Names Use Comma Example Kapil,Bigboss,Movies')
        slow_writter(f' {lpink} At The End Use ,,, types comma Example Kapil,Bigboss,Movies,,,')
        print(c * f'{lcyan}-{stop}')
        groups_names = input(f' {lgreen}Put Groups Names Using Comma (,) {stop}: ').replace(' ', '+').split(',')
        for groups_name in groups_names:
            po = self.data_http(groups_name)
            if po is not None and 'Your network' in po:
                print(po)
            else:
                finding_tags = set(re.findall('"strong_id__":null,"recent_search_entity_value":{"__typename":"Group","id":"(.*?)","name":"(.*?)",',str(po)))
                for group_id, group_name in finding_tags:
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode-escape')
                    except:
                        group_name = group_name
                    group_name = ''.join(c if unicodedata.category(c)[0] in ['L', 'N', 'Z'] else '?' for c in group_name)
                    print(f'{lgreen} SucessFully Obtained {yellow}{group_id}{stop} | {yellow}{group_name}{stop} ')
                    total.append(group_name)
                    self.namefile.write(group_id + '|' + group_name + '\n')
        end_result(self.filenm)

    def group_by_id(self):
        if len(self.file) < 1:
            slow_writter(f' {lpink} Paste All Groups Ids To input_data.txt File Then It Will Start')
            print(c * f'{lcyan}-{stop}')
            exit()
        for groups_name in self.file:
            try:
                po = requests.get(f'https://web.facebook.com/groups/{groups_name}/about', headers=self.headers2).text
            except requests.exceptions.ConnectionError:
                print(f'{red} Your network is slow due to that tool also work slow {stop}')
                time.sleep(7)
            groups_name = re.search(r':"Group","name":"(.*?)",', str(po)).group(1)
            po = self.data_http(groups_name)
            if po is not None and 'Your network' in po:
                print(po)
            else:
                finding_tags = set(re.findall('"strong_id__":null,"recent_search_entity_value":{"__typename":"Group","id":"(.*?)","name":"(.*?)",',str(po)))
                for group_id, group_name in finding_tags:
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode-escape')
                    except:
                        group_name = group_name
                    group_name = ''.join(
                        c if unicodedata.category(c)[0] in ['L', 'N', 'Z'] else '?' for c in group_name)
                    print(f'{lgreen} SucessFully Obtained {yellow}{group_id}{stop} | {yellow}{group_name}{stop} ')
                    self.namefile.write(group_id + '|' + group_name + '\n')
                    total.append(group_name)
        end_result(self.filenm)


    def group_by_country(self):
        print(f' {lpink} For Multiple Names Use Comma Example Kapil,Bigboss,Movies')
        print(f' {lpink} At The End Use ,,, types comma Example Kapil,Bigboss,Movies,,,')
        print(c * f'{lcyan}-{stop}')
        groups_names = input(f' {lgreen}Put Groups Names Using Comma (,) {stop}: ').replace(' ', '+').split(',')
        country_by_users = input(f' {lyellow}Put Country Names Using Comma (,) {stop}: ').replace(' ', '+').split(',')
        page_ids_and_names = []
        for groups_name in groups_names:
            for country_by_user in country_by_users:
                data = {
                    'client_doc_id': '26181989761915706844914575290',
                    'method': 'post',
                    'locale': 'en_US',
                    'pretty': 'false',
                    'format': 'json',
                    'variables': '{"count":12,"profile_picture_size":72,"filterID":"Z3NxZjp7IjAiOiJicm93c2VfaW5zdGFudF9maWx0ZXIiLCIxIjoia2V5d29yZHNfZ3JvdXBzKGxpb24pIiwiMyI6Ijg3OGJhMDEzLWY0ZTctNDczZi1hMjQ1LTkwMTQzNWZjZTQ2YiIsImN1c3RvbV92YWx1ZSI6IkJyb3dzZUdyb3Vwc0NpdHlJbnN0YW50RmlsdGVyQ3VzdG9tVmFsdWUifQ==","substring":"' + country_by_user + '","location_filter_fetch":true}',
                    'fb_api_req_friendly_name': 'FB4AGraphSearchFilterQuery',
                    'fb_api_caller_class': 'graphservice',
                    'fb_api_analytics_tags': '["GraphServices"]',
                    'server_timestamps': 'true'
                }
                try:
                    po = requests.post('https://graph.facebook.com/graphql?', headers=self.headers, data=data).json()
                    node = po['data']['node']
                    for edge in node['filter_values']['edges']:
                        page = edge['node']['value_object']
                        page_ids_and_names.append(page['id'])
                    for i in range(len(page_ids_and_names)):
                        id = page_ids_and_names[i]
                        data2 = {
                            "client_doc_id": "395907910716176498299001478287",
                            "method": "post",
                            "locale": "en_US",
                            "pretty": "false",
                            "format": "json",
                            "variables": "{\"default_image_scale\":3,\"bsid\":\"c6f54b43-f131-4db4-a60f-8b8f9eebf42f\",\"entered_query_text\":\"\",\"image_low_width\":240,\"image_large_aspect_height\":376,\"disable_story_menu_actions\":false,\"query_source\":\"unknown\",\"ui_theme_name\":\"\",\"image_medium_width\":360,\"product_item_image_size\":342,\"image_high_width\":720,\"nt_context\":{\"using_white_navbar\":true,\"pixel_ratio\":3,\"styles_id\":\"c86e2eaa6c16a4f0fa7d2a955a7a8004\",\"bloks_version\":\"f7474c5acff3b37762d44692791f804159a49cf699021ba3623bcb76ea1576a2\"},\"scale\":\"3\",\"enable_at_stream\":true,\"callsite\":\"android:group_search\",\"bqf\":\"keywords_groups(" + groups_name + ")\",\"tsid\":\""'' + id + ''"\",\"first_unit_only\":true,\"supported_experiences\":[\"FAST_FILTERS\",\"FILTERS\",\"FILTERS_AS_SEE_MORE\",\"INSTANT_FILTERS\",\"MARKETPLACE_ON_GLOBAL\",\"MIXED_MEDIA\",\"NATIVE_TEMPLATES\",\"NT_ENABLED_FOR_TAB\",\"NT_SPLIT_VIEWS\",\"PHOTO_STREAM_VIEWER\",\"SEARCH_SNIPPETS_ICONS_ENABLED\",\"USAGE_COLOR_SERP\",\"commerce_groups_search\",\"keyword_only\"],\"filters\":[{\"value\":\"{\\\"name\\\":\\\"filter_groups_location\\\",\\\"args\\\":\\\""'' + id + ''"\\\"}\",\"name\":\"filter_groups_location\",\"handle\":\"\",\"action\":\"add\"},{\"value\":\"{\\\"name\\\":\\\"groups_tab\\\",\\\"args\\\":\\\"\\\"}\",\"name\":\"tab_filter\",\"handle\":\"\",\"action\":\"add\"}],\"request_index\":0,\"profile_image_size\":212,\"network_start_time\":\"1681164769554\",\"image_large_aspect_width\":720,\"inline_comments_location\":\"search\"}",
                            "fb_api_req_friendly_name": "SearchResultsGraphQL-main_query",
                            "fb_api_caller_class": "graphservice",
                            "fb_api_analytics_tags": "[\"main_query\",\"GraphServices\"]",
                            "server_timestamps": "true"
                        }
                        po = requests.post('https://graph.facebook.com/graphql?', headers=self.headers, data=data2).text
                        finding_tags = set(re.findall('"strong_id__":null,"recent_search_entity_value":{"__typename":"Group","id":"(.*?)","name":"(.*?)",',str(po)))
                        for group_id, group_name in finding_tags:
                            try:
                                group_name = group_name.encode('utf-8').decode('unicode-escape')
                            except:
                                group_name = group_name
                            group_name = ''.join(
                                c if unicodedata.category(c)[0] in ['L', 'N', 'Z'] else '?' for c in group_name)
                            print(f'{lgreen} SucessFully Obtained {yellow}{group_id}{stop} | {yellow}{group_name}{stop} ')
                            total.append(group_name)
                            self.namefile.write(group_id + '|' + group_name + '\n')
                except requests.exceptions.ConnectionError:
                    print(f'{red} Your network is slow due to that tool also work slow {stop}')
                    time.sleep(7)
        end_result(self.filenm)

class main_nologin():
    def __init__(self):
        stm(cls)
        print(logo)
        from developer_file_donot_open import headers_agents
        self.config = json.load(open('config.json', 'r'))
        self.headers2 = headers_agents.headers2()
        self.filenm = datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
        self.namefile = open(f'data/{self.filenm}.txt', 'a', encoding='utf-8')
        self.file = open('input_data.txt', 'r').readlines()

    def extract_pure_active(self):
        minimum_posts_per_day = self.config['posts_per_day']
        for group_id in self.file:
            group_id = group_id.replace('\n', '')
            po = requests.get(f'https://web.facebook.com/groups/{group_id}/about', headers=self.headers2).text
            int(group_id.strip())
            try:
                total_members = re.search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
                posts_per_day = re.search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
                group_name = re.search(r':"Group","name":"(.*?)",', str(po)).group(1)
                try:
                    group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
                except (ValueError, UnicodeEncodeError):
                        pass
                if int(posts_per_day) > int(minimum_posts_per_day):
                    total.append(group_name)
                    print(f'{lpink} Extracted {yellow}{group_id}{stop} | {yellow}{group_name}{stop} | {lgreen}Active{stop} | {yellow}{total_members}{stop}')
                    self.namefile.write(group_id + '|' + group_name + '|' + 'Active' + '|' + total_members + '\n')
                else:
                    print(f'{lpink} Extracted {yellow}{group_id}{stop} | {yellow}{group_name}{stop} | {lred}Deadzz{stop} | {yellow}{total_members}{stop}')
            except IndexError:
                print(' something went wrong with this group {}'.format(group_id))
            except requests.exceptions.ConnectionError:
                print(f'{red} Your network is slow due to that tool also work slow {stop}')
                time.sleep(7)
        end_result(self.filenm)

    def extract_auto_approval(self):
        minimum_posts_per_day = self.config['auto_approvals_posts']
        for group_id in self.file:
            group_id = group_id.replace('\n', '')
            po = requests.get(f'https://web.facebook.com/groups/{group_id}/about', headers=self.headers2).text
            int(group_id.strip())
            try:
                total_members = re.search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
                posts_per_day = re.search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
                group_name = re.search(r':"Group","name":"(.*?)",', str(po)).group(1)
                try:
                    group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
                except (ValueError, UnicodeEncodeError):
                        pass
                if int(posts_per_day) > int(minimum_posts_per_day):
                    total.append(group_name)
                    print(f'{lpink} Extracted {yellow}{group_id}{stop} | {yellow}{group_name}{stop} | {lgreen}Auto Approval{stop} | {yellow}{total_members}{stop}')
                    self.namefile.write(group_id + '|' + group_name + '|' + 'Auto Approve' + '|' + total_members + '\n')
                else:
                    print(f'{lpink} Extracted {yellow}{group_id}{stop} | {yellow}{group_name}{stop} | {lred}Admin Approval{stop} | {yellow}{total_members}{stop}')
            except IndexError:
                print(' something went wrong with this group {}'.format(group_id))
            except requests.exceptions.ConnectionError:
                print(f'{red} Your network is slow due to that tool also work slow {stop}')
                time.sleep(7)
        end_result(self.filenm)


if __name__ == '__main__':
    main_dashboard()