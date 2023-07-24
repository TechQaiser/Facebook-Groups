from os import system as stm
from time import sleep
from datetime import datetime
import json, sys, os, codecs, random, time
from re import findall, search
try:
    from requests import post, session, get, exceptions
except ModuleNotFoundError:
    stm('pip install request')
    stm('main.exe')
try:
    from rich.panel import Panel
    from rich.style import Style
    from rich.console import Console
    from rich.columns import Columns
    from rich.table import Table
    from rich.tree import Tree
except ModuleNotFoundError:
    stm('pip install rich')
    stm('main.exe')

console = Console()
cpr = console.print
stm("mode con: cols=96")
next_pages = []
total = []

"""
The Headers Def Use To Post Or Get Requests:
Each Def Have Its Own Values To Return
"""
chromium = f'112.0.{str(random.randint(5200,5900))}.{str(random.randint(120,390))}'
def agent()-> str:
    return f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chromium} Safari/537.36'
def head1():
    headers: dict = {
        'Host': 'web.facebook.com',
        'Cookie': 'a',
        'Cache-Control': 'max-age=0',
        'Viewport-Width': '838',
        'Sec-Ch-Ua': f'"Not:A-Brand";v="99", "Chromium";v="{chromium}"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
        'Sec-Ch-Ua-Full-Version-List': f'"Not:A-Brand";v="99.0.0.0", "Chromium";v=f"{chromium}"',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://web.facebook.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
}
    return headers

def head2(searchtext):
    headers: dict = {
        'Host': 'web.facebook.com',
        'Cookie': 'fr=0lUmEt5IspmPaHaPV.AWX_bHYa7tedObgtJdgyVprGfKo.BkQ5q1.IL.AAA.0.0.BkVAd8.AWUOoLVBF14; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1683232081740%2C%22v%22%3A1%7D; wd=838x897',
        'Content-Length': '4753',
        'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': agent(),
        'Viewport-Width': '838',
        'X-Fb-Friendly-Name': 'SearchCometResultsPaginatedResultsQuery',
        'X-Fb-Lsd': 'MVl',
        'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Asbd-Id': '198387',
        'Sec-Ch-Ua-Full-Version-List': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="'+str(chromium)+'"',
        'Sec-Ch-Prefers-Color-Scheme': 'light',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://web.facebook.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://web.facebook.com/search/groups/?q={searchtext}',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    return headers
try:
    details = get('https://raw.githubusercontent.com/TechQaiser/TechQaiser/main/Facebook-Groups/data_for_fb_groups/data.json').json()
    version = details['version']
    number = details['number']
    link = details['link']
    obtain = get(link).text
    original_password = search(r'name="pas">(.*?)</h3>', str(obtain)).group(1)
except exceptions.ConnectionError:
    cpr(Panel(' You Have No Internet Connection Kindly Connect Network And Run Tool Again', border_style='red'))

def logo():
    stm('cls')
    logos = f"""
      ███████ ██████         ██████  ██████   ██████  ██    ██ ██████        ██████  
      ██      ██   ██       ██       ██   ██ ██    ██ ██    ██ ██   ██            ██ 
      █████   ██████  █████ ██   ███ ██████  ██    ██ ██    ██ ██████  █████  █████  
      ██      ██   ██       ██    ██ ██   ██ ██    ██ ██    ██ ██            ██      
      ██      ██████         ██████  ██   ██  ██████   ██████  ██            ███████ 
      ------------------------------------------------------------------------------
          You Can Help Me By Donating 2 Me :-( >>> Easypaisa,Jazzcash {number}
      ------------------------------------------------------------------------------
"""
    lo = Panel(f"[#d78700]{logos}", style='#afffff')
    details = f"""
   Tool Version : [white]{version}[/white]
   Credit       : [white]QSR Owner[/white]
   Tool Status  : [white]Working Enjoy[/white]
   License      : [white]Approved[/white]
"""
    detail = Panel(f"[#d78700]{details}", style='#afffff', title='[#d700d7]Social Media')
    abouts = """
   Facebook : Qaiser Abbas
   Telegram : @ASHUInsights
   Github   :  TechQaiser
   Youtube : Tech Qaiser
"""
    about = Panel(f"[#d78700]{abouts}", style='#afffff', title='[#d700d7]Tool Status')
    columns = Columns([detail, about], expand=True)
    cpr(lo)
    cpr(columns)

def password_checker():
    try:
        file_password = open('modules/.username.txt','r').read()
        if file_password == original_password:
            pass
        else:
            stm('clear')
            logo()
            cpr(Panel(f'        Put Password Of Tool Here , Get Password Of Tool From This Link!!! \n          {link}',border_style='magenta'))
            password = console.input('             ┗──[cyan]Put Password Of Tool [/cyan] : ')
            if password == original_password:
                open('modules/.username.txt', 'w').write(original_password)
                stm('clear')
                logo()
                cpr(Panel('                         Sucessfully Login Done ;-X !', border_style='green'))
                sleep(4)
            else:
                stm('clear')
                logo()
                cpr(Panel('              Invalid Password Try Again ! Visit Website To Get Password', border_style='red'))
                sleep(4)
                password_checker()
    except Exception as e:
        exit(e)

password_checker()

def link_checker_post(link, data, header, cookies):
    while True:
        try:
            po = post(link, data=data, headers=header, cookies={'Cookie' : cookies}).text
            return po
        except exceptions.ConnectionError:
            pass

def link_checker_get(link, header, cookies):
    while True:
        try:
            po = get(link, headers=header).text
            return po
        except exceptions.ConnectionError:
            pass

def CHmy_FILES(folder: list):
    for file in folder:
        files = "modules/"+file
        if not os.path.exists(files):
            cpr(Panel('              Missing Files From Your Folder Re-Download Files Again',border_style='red'))
            sys.exit()

def groups_name(file,headers, cookies):
    if len(file) < 1:
        cpr(Panel(f'   Paste All Groups Ids To input_data.txt File Then It Will Start ', border_style='#ff005f'))
    for groups_name in file:
        po = link_checker_get(f'https://web.facebook.com/groups/{groups_name}/about', headers, cookies)
        groups_name = search(r':"Group","name":"(.*?)",', str(po)).group(1)
        return groups_name

def country_ARGS(head: dict, iid: str, f: str, j: str, l: int, countrys: list, cookies: str) -> list:
    lists=[]
    for country in countrys:
        data = {'av': [iid], '__user': [iid], '__comet_req': ['15'], 'fb_dtsg': [f], 'jazoest': [j], 'lsd': [l], 'fb_api_caller_class': ['RelayModern'], 'fb_api_req_friendly_name': ['useSearchCometFilterTypeaheadTypedDataSourceQuery'], 'variables': ['{"count":8,"filterID":"Z3NxZjp7IjAiOiJicm93c2VfaW5zdGFudF9maWx0ZXIiLCIxIjoia2V5d29yZHNfZ3JvdXBzKHRvdGFsK2dhbWluZykiLCIzIjoiYTZmZjVmZjMtNGU1Mi00ZjVlLTlkZGEtMGE3YTkwYzVhNWY3IiwiY3VzdG9tX3ZhbHVlIjoiQnJvd3NlR3JvdXBzQ2l0eUluc3RhbnRGaWx0ZXJDdXN0b21WYWx1ZSJ9","query":"'+country+'"}'], 'server_timestamps': ['true'], 'doc_id': ['8960381707365732']}
        obtain = link_checker_post('https://web.facebook.com/api/graphql/', data, head, cookies)
        FOUNDEDX_Result = findall(',"__isActor":"Page","id":"(.*?)"', str(obtain))
        for foundid in FOUNDEDX_Result:
            lists.append(foundid)
    return lists

def end_resuls(end, strt):
    elapsed_time = end - strt
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    return cpr(Panel(f'\n                             Process Finished Sucessfully       \n           Total Groups Done / Total Time Taken : [cyan]{len(total)}[/cyan] / Minutes|Seconds : [cyan]{minutes, seconds}[/cyan]',border_style='green', title='[yellow]Here Is Details[/yellow]'))

def main():
    stm('cls')
    logo()
    table = Table(expand=True)
    table.add_column('[#d78700]   Keyword    ', justify='center')
    table.add_column('[#d78700] Main Title  ', justify='center')
    table.add_column('[#d78700] Login Require  ', justify='center')
    table.add_row("  1   ", " Find Groups By Names","   [#d78700]Yes[/#d78700]")
    table.add_row("  2   ", " Find Groups By Group Ids", "   [#d78700]Yes[/#d78700]")
    table.add_row("  3   ", " Find Groups By Country", "   [#d78700]Yes[/#d78700]")
    table.add_row("  4   ", " Find Groups Without Admins", "   [green]No[/green]")
    table.add_row("  5   ", " Seprate Groups Auto-Approval", "   [green]No[/green]")
    table.add_row("  6   ", " Seprate Groups Highly Active", "   [green]No[/green]")
    table.add_row("  7   ", " Seprate Groups Minimum Members", "   [green]No[/green] ")
    table.add_row("  8   ", " Logout Old Cookie ")
    table.add_row("  S   ", " Use Spliter To Split Ids ")
    table.add_row("  0   ", " Exit Tool")
    cpr(table)
    user_select = console.input('             ┗──[#d78700]Select Choice[/#d78700] : ')
    if user_select in ['1', '01']:
        NEED_to_login_class().FIND____NAMES()
    elif user_select in ['2', '02']:
        NEED_to_login_class().FIND____ID()
    elif user_select in ['3', '03']:
        NEED_to_login_class().FIND___BY_COUNTRYOFFSET()
    elif user_select in ['4', '04']:
        NO_LOGIN_required().GROUP___NOADMINS()
    elif user_select in ['5', '05']:
        NO_LOGIN_required().SEPRATE___AUTOAPPROVAL()
    elif user_select in ['6', '06']:
        NO_LOGIN_required().SEPRATE___ACTIVE()
    elif user_select in ['7', '07']:
        NO_LOGIN_required().SEPRATE___MEMBERS()
    elif user_select in ['S', 's']:
        path = '../.Results_output/spliter.txt'
        if os.path.exists(path):
            os.remove(path)
        while True:
            put = input("Paste Your Data Here : ")
            if put in ['', ' ']:
                cpr(Panel('                         Sucessfully Xtracted All Lists', border_style='green'))
                break
            print(put.split('|')[0])
            open(f'./Results_output/{datetime.now().strftime("%Y-%m-%d.%H.%M.%S")}.txt','a', encoding='utf-8').write(put.split('|')[0] + '\n')
    elif user_select in ['8', '08']:
        stm('clear')
        logo()
        open('modules/cookie.txt', 'w').write(' ')
        cpr(Panel('                         Old Id Cookies Removed Sucessfully', border_style='green'))
        sleep(5)
        stm('main.exe')
    else:
        stm('clear')
        logo()
        cpr(Panel('                         Thanks For Using Our Tools', border_style='#ff005f'))

def login():
    stm('cls')
    logo()
    cookie = console.input(' > Paste Cookies Here : ')
    if len(cookie) < 50:
        cpr(Panel('                         Invalid Cookies Inputed !!!', border_style='#ff005f'))
    else:
        obtain = get('https://www.facebook.com/', cookies={"Cookies": cookie}).text
        try:
            fb_dtsg = search('DTSGInitialData(.*?):"(.*?)"', obtain).group(2)
            if len(fb_dtsg) < 20:
                cpr(Panel('                         You Pasted Invalid Or Expire Cookie', border_style='#ff005f'))
                sleep(3)
                login()
            else:
                if "locale=en_US" not in cookie:
                    cookie += "locale=en_US;"
                    open('modules/cookie.txt', 'w').write(cookie)
                    cpr(Panel('                         Sucessfully Login Done ;-X !', border_style='green'))
                    sleep(4)
                    stm('main.exe')
                else:
                    open('modules/cookie.txt','w').write(cookie)
                    cpr(Panel('                         Sucessfully Login Done ;-X !', border_style='green'))
                    stm('main.exe')
        except:
            cpr(Panel('                         Cookies Are Not Valid Login Again !', border_style='#ff005f'))
            sleep(3)

class NEED_to_login_class():
    def __init__(self):
        stm('cls')
        logo()
        self.config = json.load(open('modules/config.json', 'r'))
        self.cookies = open('modules/cookie.txt','r').read()
        self.data = open('modules/input_data.txt','r').readlines()
        self.namefile = datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
        try:
            obtain = get('https://www.facebook.com/',cookies={"Cookies":self.cookies}).text
            try:
                fb_dtsg = search('DTSGInitialData(.*?):"(.*?)"', obtain).group(2)
                if len(fb_dtsg) < 20:
                    cpr(Panel('                         Cookies Are Not Valid Login Again !', border_style='#ff005f'))
                    sleep(3)
                    login()
            except:
                cpr(Panel('                         Cookies Are Not Valid Login Again !', border_style='#ff005f'))
                sleep(3)
                login()
            else:
                self.fb_dtsg = search('DTSGInitialData(.*?):"(.*?)"', obtain).group(2)
                self.jazoest = search('&__comet_req=15&jazoest=(.*?)"', obtain).group(1)
                self.lsd = search('LSD(.*?):"(.*?)"', obtain).group(2)
                try:
                    self.uid = search('c_user=(.*?);', str(self.cookies)).group(1)
                except:
                    self.uid = search('m_page_voice=(.*?);', str(self.cookies)).group(1)
        except Exception as eL:
            print(eL)
            sys.exit()
    def FIND____NAMES(self):
        cpr(Panel('        Use , For Multiple Names/Keywords Like Shahid Afridi,MS Dhoni,Babar Azam, etc',border_style='magenta'))
        search_keyword = console.input('[#87ffff] Put Names Use (,) For multiple Names [/#87ffff]: ').replace(' ', '%20').split(',')
        headers = head1()
        headers['Cookie'] = self.cookies
        obtain = link_checker_get(f'https://web.facebook.com/search/groups/?q={search_keyword}', headers, self.cookies)
        start_time = time.time()
        if '"end_cursor"' in obtain:
            getting_groups = findall('"complete":true,"result":{"data"(.*?)"cursor":null}],"filters"', str(obtain))[0]
            group_id = findall(r'"type":"Group","id":"(.*?)"', str(getting_groups))
            group_name = findall(r'"profile_name_with_possible_nickname":"(.*?)"', str(getting_groups))
            gp_d = findall(r'"prominent_snippet_text_with_entities":null,(.*?)"},"description', str(getting_groups))
            group_activity = findall('"text":"(.*?)\'', str(gp_d))
            next_page = findall('"end_cursor":"(.*?)"', str(obtain))
            for ops in range(len(group_id)):
                try:
                    group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
                except:
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode-escape')
                    except:
                        group_name = group_name
                if len(str(group_name)) > 25:
                    group_name = group_name[:20]
                else:
                    group_name = group_name
                bolder = Style(bold=True)
                open(f'./Results_output/{self.namefile}.txt','a', encoding='utf-8').write(group_id[ops]+' | '+group_name[ops]+' | '+group_activity[ops].replace('\\\\u00b7', ' ').replace('\\u00e9','ate').replace('\\u00a0K','K')+'\n')
                cpr(Panel("[bold green]%s[/bold green] | [bold yellow]%s[/bold yellow] | [#87ffff]%s[/#87ffff]" % (group_id[ops], group_name[ops], group_activity[ops].replace('\\\\u00b7', ' ').replace('\\u00e9','ate').replace('\\u00a0K','K')), style=bolder, border_style='white'))
                total.append(group_name)
            next_pages.append(next_page)
            for i in range(len(search_keyword)):
                for lll in range(int(self.config['pages_for_single_group'])):
                    for page_change in next_pages:
                        headers = head2(search_keyword[i])
                        headers['X-Fb-Lsd'] = self.lsd
                        data = {'av': [self.uid], '__user': [self.uid], 'fb_dtsg': [self.fb_dtsg],'jazoest': [self.jazoest], 'lsd': [self.lsd], 'fb_api_caller_class': ['RelayModern'],'fb_api_req_friendly_name': ['SearchCometResultsPaginatedResultsQuery'], 'variables': ['{"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"bea24616-fbb8-4058-b82c-5cd7110d8c13","tsid":null},"experience":{"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"' +search_keyword[i] + '"},"count":5,"cursor":"' + str(page_change[0]) + '","displayCommentsContextEnableComment":false,"displayCommentsContextIsAdPreview":false,"displayCommentsContextIsAggregatedShare":false,"displayCommentsContextIsStorySet":false,"displayCommentsFeedbackContext":null,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__SearchCometResultsShowUserAvailabilityrelayprovider":true,"__relay_internal__pv__GroupsCometDelayCheckBlockedUsersrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}'],'server_timestamps': ['true'], 'doc_id': ['10012182385474413']}
                        headers['Cookie'] = self.cookies
                        po = link_checker_post('https://web.facebook.com/api/graphql/', data, headers, self.cookies)
                        group_id = findall(r'"type":"Group","id":"(.*?)"', str(po))
                        group_name = findall(r'"profile_name_with_possible_nickname":"(.*?)"', str(po))
                        group_activity = findall('"text":"(.*?)\'', str(findall(r'"prominent_snippet_text_with_entities":null,(.*?)"},"description', str(po))))
                        next_pagee = findall('"end_cursor":"(.*?)"', str(po))
                        for ching in range(len(group_id)):
                            try:
                                try:
                                    group_name = group_name.encode('utf-8').decode('unicode-escape')
                                except:
                                    try:
                                        group_name = group_name.encode('utf-8').decode('unicode_escape')
                                    except:
                                        group_name = group_name
                                if len(str(group_name)) > 25:
                                    group_name = group_name[:20]
                                else:
                                    group_name = group_name
                                bolder = Style(bold=True)
                                cpr(Panel(
                                    "[bold green]%s[/bold green] | [bold yellow]%s[/bold yellow] | [#87ffff]%s[/#87ffff]" % (
                                        group_id[ching], group_name[ching],
                                        group_activity[ching].replace('\\\\u00b7', ' ').replace('\\u00e9',
                                                                                                'ate').replace(
                                            '\\u00a0K', 'K')), style=bolder, border_style='white'))
                                open(f'./Results_output/{self.namefile}.txt', 'a', encoding='utf-8').write(
                                    group_id[ching] + ' | ' + group_name[ching] + ' | ' + group_activity[ching].replace(
                                        '\\\\u00b7', ' ').replace('\\u00e9', 'ate').replace('\\u00a0K', 'K') + '\n')
                                total.append(group_name[ching])
                            except IndexError:
                                cpr(Panel(f'                        Keyword Fault Or Id Fault (Test 3 Option)',
                                          border_style='#ff005f'))
                        next_pages.remove(page_change)
                        next_pages.append(next_pagee)
        else:
            cpr(Panel(f'                        Something Went wrong Try Again', border_style='#ff005f'))
        end_time = time.time()
        end_resuls(end_time, start_time)

    def FIND____ID(self):
        headers = head1()
        headers['Cookie'] = self.cookies
        search_keyword = groups_name(self.data, headers, self.cookies).replace(' ','%20')
        obtain = link_checker_get(f'https://web.facebook.com/search/groups/?q={search_keyword}', headers, self.cookies)
        start_time = time.time()
        if '"end_cursor"' in obtain:
            getting_groups = findall('"complete":true,"result":{"data"(.*?)"cursor":null}],"filters"', str(obtain))[0]
            group_id = findall(r'"type":"Group","id":"(.*?)"', str(getting_groups))
            group_name = findall(r'"profile_name_with_possible_nickname":"(.*?)"', str(getting_groups))
            gp_d = findall(r'"prominent_snippet_text_with_entities":null,(.*?)"},"description', str(getting_groups))
            group_activity = findall('"text":"(.*?)\'', str(gp_d))
            next_page = findall('"end_cursor":"(.*?)"', str(obtain))
            for ops in range(len(group_id)):
                try:
                    group_name = group_name.encode('utf-8').decode('unicode-escape')
                except:
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode_escape')
                    except:
                        group_name = group_name
                if len(str(group_name)) > 25:
                    group_name = group_name[:20]
                else:
                    group_name = group_name
                bolder = Style(bold=True)
                open(f'./Results_output/{self.namefile}.txt', 'a', encoding='utf-8').write(group_id[ops] + ' | ' + group_name[ops] + ' | ' + group_activity[ops].replace('\\\\u00b7',' ').replace('\\u00e9', 'ate').replace('\\u00a0K', 'K') + '\n')
                cpr(Panel("[bold green]%s[/bold green] | [bold yellow]%s[/bold yellow] | [#87ffff]%s[/#87ffff]" % (
                group_id[ops], group_name[ops], group_activity[ops].replace('\\\\u00b7', ' ').replace('\\u00e9','ate').replace('\\u00a0K','K')), style=bolder,
                          border_style='white'))
                total.append(group_name)
            next_pages.append(next_page)
            for i in range(len(self.data)):
                for page_change in next_pages:
                    headers = head2(search_keyword)
                    headers['X-Fb-Lsd'] = self.lsd
                    data = {'av': [self.uid], '__user': [self.uid], 'fb_dtsg': [self.fb_dtsg],
                                'jazoest': [self.jazoest], 'lsd': [self.lsd], 'fb_api_caller_class': ['RelayModern'],
                                'fb_api_req_friendly_name': ['SearchCometResultsPaginatedResultsQuery'], 'variables': [
                                '{"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"bea24616-fbb8-4058-b82c-5cd7110d8c13","tsid":null},"experience":{"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"' +
                                search_keyword + '"},"count":5,"cursor":"' + str(page_change[
                                                                                        0]) + '","displayCommentsContextEnableComment":false,"displayCommentsContextIsAdPreview":false,"displayCommentsContextIsAggregatedShare":false,"displayCommentsContextIsStorySet":false,"displayCommentsFeedbackContext":null,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__SearchCometResultsShowUserAvailabilityrelayprovider":true,"__relay_internal__pv__GroupsCometDelayCheckBlockedUsersrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}'],
                                'server_timestamps': ['true'], 'doc_id': ['10012182385474413']}
                    headers['Cookie'] = self.cookies
                    po = link_checker_post('https://web.facebook.com/api/graphql/', data, headers, self.cookies)
                    group_id = findall(r'"type":"Group","id":"(.*?)"', str(po))
                    group_name = findall(r'"profile_name_with_possible_nickname":"(.*?)"', str(po))
                    group_activity = findall('"text":"(.*?)\'', str(findall(
                            r'"prominent_snippet_text_with_entities":null,(.*?)"},"description', str(po))))
                    next_pagee = findall('"end_cursor":"(.*?)"', str(po))
                    for ching in range(len(group_id)):
                        try:
                            group_name = group_name.encode('utf-8').decode('unicode-escape')
                        except:
                            try:
                                group_name = group_name.encode('utf-8').decode('unicode_escape')
                            except:
                                group_name = group_name
                        if len(str(group_name)) > 25:
                            group_name = group_name[:20]
                        else:
                            group_name = group_name
                        bolder = Style(bold=True)
                        cpr(Panel("[bold green]%s[/bold green] | [bold yellow]%s[/bold yellow] | [#87ffff]%s[/#87ffff]" % (group_id[ching], group_name[ching], group_activity[ching].replace('\\\\u00b7', ' ').replace('\\u00e9','ate').replace('\\u00a0K','K')),style=bolder, border_style='white'))
                        open(f'./Results_output/{self.namefile}.txt', 'a', encoding='utf-8').write(group_id[ching] + ' | ' + group_name[ching] + ' | ' + group_activity[ching].replace('\\\\u00b7', ' ').replace('\\u00e9', 'ate').replace('\\u00a0K', 'K') + '\n')
                        total.append(group_name[ching])
                    next_pages.remove(page_change)
                    next_pages.append(next_pagee)
        else:
            cpr(Panel(f'                        Something Went wrong Try Again', border_style='#ff005f'))
        end_time = time.time()
        end_resuls(end_time, start_time)

    def FIND___BY_COUNTRYOFFSET(self):
        cpr(Panel('        Use , For Multiple Names/Keywords Like Shahid Afridi,MS Dhoni,Babar Azam, etc',border_style='magenta'))
        search_keyword = console.input('[#87ffff] Put Names Use (,) For multiple Names [/#87ffff]: ').replace(' ','%20').split(',')
        country_NAMES = console.input('[cyan] Put Country Names - Use Comma For Multi [/cyan]: ').split(',')
        headers = head1()
        headers['Cookie'] = self.cookies
        country_names = country_ARGS(headers, self.uid, self.fb_dtsg, self.jazoest, self.lsd, country_NAMES, self.cookies)
        obtain = link_checker_get(f'https://web.facebook.com/search/groups/?q={search_keyword}', headers, self.cookies)
        start_time = time.time()
        if '"end_cursor"' in obtain:
            getting_groups = findall('"complete":true,"result":{"data"(.*?)"cursor":null}],"filters"', str(obtain))[0]
            group_id = findall(r'"type":"Group","id":"(.*?)"', str(getting_groups))
            group_name = findall(r'"profile_name_with_possible_nickname":"(.*?)"', str(getting_groups))
            gp_d = findall(r'"prominent_snippet_text_with_entities":null,(.*?)"},"description', str(getting_groups))
            group_activity = findall('"text":"(.*?)\'', str(gp_d))
            next_page = findall('"end_cursor":"(.*?)"', str(obtain))
            for ops in range(len(group_id)):
                try:
                    group_name = group_name.encode('utf-8').decode('unicode-escape')
                except:
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode_escape')
                    except:
                        group_name = group_name
                if len(str(group_name)) > 25:
                    group_name = group_name[:20]
                else:
                    group_name = group_name
                bolder = Style(bold=True)
                open(f'./Results_output/{self.namefile}.txt', 'a', encoding='utf-8').write(group_id[ops] + ' | ' + group_name[ops] + ' | ' + group_activity[ops].replace('\\\\u00b7',' ').replace('\\u00e9', 'ate').replace('\\u00a0K', 'K') + '\n')
                cpr(Panel("[bold green]%s[/bold green] | [bold yellow]%s[/bold yellow] | [#87ffff]%s[/#87ffff]" % (
                group_id[ops], group_name[ops], group_activity[ops].replace('\\\\u00b7', ' ').replace('\\u00e9','ate').replace('\\u00a0K','K')), style=bolder,
                          border_style='white'))
                total.append(group_name)
            next_pages.append(next_page)
            for i in range(len(search_keyword)):
                for lll in range(int(self.config['pages_for_single_group'])):
                    for country_name in country_names:
                        for page_change in next_pages:
                            headers = head2(search_keyword[i])
                            headers['X-Fb-Lsd'] = self.lsd
                            data = {'av': [self.uid], '__user': [self.uid],'fb_dtsg': [self.fb_dtsg],'jazoest': [self.jazoest], 'lsd': [self.lsd], 'variables': ['{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"8b04e379-ab6c-4586-8f4f-a87c613f85dc","tsid":null},"experience":{"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":["{\\"name\\":\\"filter_groups_location\\",\\"args\\":\\"' + country_name + '\\"}"],"text":"' +search_keyword[i] + '"},"cursor":null,"feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__SearchCometResultsShowUserAvailabilityrelayprovider":true,"__relay_internal__pv__GroupsCometDelayCheckBlockedUsersrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__StoriesRingrelayprovider":false}'],'server_timestamps': ['true'], 'doc_id': ['6699566390072927']}
                            headers['Cookie'] = self.cookies
                            po = link_checker_post('https://web.facebook.com/api/graphql/', data, headers, self.cookies)
                            group_id = findall(r'"type":"Group","id":"(.*?)"', str(po))
                            group_name = findall(r'"profile_name_with_possible_nickname":"(.*?)"', str(po))
                            group_activity = findall('"text":"(.*?)\'', str(findall(r'"prominent_snippet_text_with_entities":null,(.*?)"},"description', str(po))))
                            next_pagee = findall('"end_cursor":"(.*?)"', str(po))
                            for ching in range(len(group_id)):
                                try:
                                    group_name = group_name.encode('utf-8').decode('unicode-escape')
                                except:
                                    try:
                                        group_name = group_name.encode('utf-8').decode('unicode_escape')
                                    except:
                                        group_name = group_name
                                if len(str(group_name)) > 25:
                                    group_name = group_name[:20]
                                else:
                                    group_name = group_name
                                bolder = Style(bold=True)
                                open(f'./Results_output/{self.namefile}.txt', 'a', encoding='utf-8').write(group_id[ching] + ' | ' + group_name[ching] + ' | ' + group_activity[ching].replace('\\\\u00b7', ' ').replace('\\u00e9', 'ate').replace('\\u00a0K', 'K') + '\n')
                                cpr(Panel("[bold green]%s[/bold green] | [bold yellow]%s[/bold yellow] | [#87ffff]%s[/#87ffff] " % (group_id[ching], group_name[ching],group_activity[ching].replace('\\\\u00b7', ' ').replace('\\u00e9','ate').replace('\\u00a0K','K')),style=bolder, border_style='white'))
                                total.append(group_name)
                            next_pages.remove(page_change)
                            next_pages.append(next_pagee)
        else:
            cpr(Panel(f'                        Something Went wrong Try Again', border_style='#ff005f'))
        end_time = time.time()
        end_resuls(end_time, start_time)

class NO_LOGIN_required():
    def __init__(self):
        stm('cls')
        logo()
        self.config = json.load(open('modules/config.json', 'r'))
        self.data = open('modules/input_data.txt', 'r').readlines()
        self.namefile = datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
    def SEPRATE___AUTOAPPROVAL(self):
        poster_day = self.config['posts_per_day']
        start_time = time.time()
        for groupids in self.data:
            group_ids = groupids.replace('\n', '')
            try:
                group_ids = group_ids.split('|')[0]
            except:
                group_ids = group_ids
            headers = head1()
            po = link_checker_get(f'https://web.facebook.com/groups/{group_ids}/about', headers, '')
            group_name = search(r':"Group","name":"(.*?)",', str(po)).group(1)
            total_members = search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
            posts_per_day = search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
            try:
                group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
            except (ValueError, UnicodeEncodeError):
                pass
            if int(posts_per_day) > int(poster_day):
                open(f'Results_output/auto_approval_{self.namefile}.txt', 'a', encoding='utf-8').write(group_ids + '|' + group_name + '|' + 'Auto Approve' + '|' + total_members + '\n')
                tree = Tree(f'Name : {group_name}', style='#00ff00')
                tree.add(f' Posts Per Day : {posts_per_day}')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#5fffff]{total_members}[/#5fffff]').add(f"Auto Approval : [#5fffff]Auto Approval[/#5fffff]")
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            else:
                tree = Tree(f'Name : {group_name}', style='#af00d7')
                tree.add(f' Posts Per Day : {posts_per_day}')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#d78700]{total_members}[/#d78700]').add(f"Auto Approval : [red]Approval Need[/red]")
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            total.append(group_name)
        end_time = time.time()
        end_resuls(end_time, start_time)

    def SEPRATE___ACTIVE(self):
        poster_day = self.config['posts_per_day']
        start_time = time.time()
        for groupids in self.data:
            group_ids = groupids.replace('\n', '')
            try:
                group_ids = group_ids.split('|')[0]
            except:
                group_ids = group_ids
            headers = head1()
            po = link_checker_get(f'https://web.facebook.com/groups/{group_ids}/about', headers, '')
            group_name = search(r':"Group","name":"(.*?)",', str(po)).group(1)
            total_members = search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
            posts_per_day = search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
            try:
                group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
            except (ValueError, UnicodeEncodeError):
                pass
            if int(posts_per_day) > int(poster_day):
                open(f'Results_output/active_groups_{self.namefile}.txt', 'a', encoding='utf-8').write(group_ids + '|' + group_name + '|' + 'Highly Active' + '|' + total_members + '\n')
                tree = Tree(f'Name : {group_name}', style='#00ff00')
                tree.add(f' Posts Per Day : {posts_per_day}')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#5fffff]{total_members}[/#5fffff]').add(f"High Active : [#5fffff]High Active[/#5fffff]")
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            else:
                tree = Tree(f'Name : {group_name}', style='#af00d7')
                tree.add(f' Posts Per Day : {posts_per_day}')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#d78700]{total_members}[/#d78700]').add(f"High Active : [red]Non Active[/red]")
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            total.append(group_name)
        end_time = time.time()
        end_resuls(end_time, start_time)

    def SEPRATE___MEMBERS(self):
        minimummembers = self.config['minimum_members_group']
        start_time = time.time()
        for groupids in self.data:
            group_ids = groupids.replace('\n', '')
            try:
                group_ids = group_ids.split('|')[0]
            except:
                group_ids = group_ids
            headers = head1()
            po = link_checker_get(f'https://web.facebook.com/groups/{group_ids}/about', headers, '')
            group_name = search(r':"Group","name":"(.*?)",', str(po)).group(1)
            total_members = search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
            try:
                total_members = total_members.replace(',', '')
            except:
                total_members = total_members
            posts_per_day = search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
            try:
                group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
            except (ValueError, UnicodeEncodeError):
                pass
            if int(total_members) > int(minimummembers):
                open(f'Results_output/total_members_{self.namefile}.txt', 'a', encoding='utf-8').write(group_ids + '|' + group_name + '|' + total_members + '\n')
                tree = Tree(f'Name : {group_name}', style='#00ff00')
                tree.add(f' Posts Per Day : {posts_per_day}')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#5fffff]{total_members}[/#5fffff]')
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            else:
                tree = Tree(f'Name : {group_name}', style='#af00d7')
                tree.add(f' Posts Per Day : {posts_per_day}')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [red]{total_members}[/red]')
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            total.append(group_name)
        end_time = time.time()
        end_resuls(end_time, start_time)

    def GROUP___NOADMINS(self):
        start_time = time.time()
        for groupids in self.data:
            group_ids = groupids.replace('\n', '')
            try:
                group_ids = group_ids.split('|')[0]
            except:
                group_ids = group_ids
            headers = head1()
            po = link_checker_get(f'https://web.facebook.com/groups/{group_ids}/about', headers, '')
            admins = findall('admin_profiles":{"count":(.*?),', str(po))[0]
            group_name = search(r':"Group","name":"(.*?)",', str(po)).group(1)
            total_members = search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', str(po)).group(1)
            posts_per_day = search(r'number_of_posts_in_last_day":(.*?),', str(po)).group(1)
            try:
                group_name = codecs.encode(group_name.encode('utf-8').decode('unicode-escape'), 'utf-16','surrogatepass').decode('utf-16')
            except (ValueError, UnicodeEncodeError):
                pass
            if int(admins) == 0:
                open(f'Results_output/without_admin_{self.namefile}.txt', 'a', encoding='utf-8').write(group_ids + '|' + group_name + '|' + total_members + '\n')
                tree = Tree(f'Name : {group_name}', style='#00ff00')
                tree.add(f' Total Admins : [#5fffff]{admins}[/#5fffff]')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#5fffff]{total_members}[/#5fffff]').add(f' Posts Per Day : {posts_per_day}')
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            else:
                tree = Tree(f'Name : {group_name}', style='#af00d7')
                tree.add(f' Total Admins : [#5fffff]{admins}[/#5fffff]')
                tree.add(f'Group Id : {group_ids}').add(f'Members : [#d78700]{total_members}[/#d78700]').add(f' Posts Per Day : {posts_per_day}')
                cpr(Panel(tree, border_style='#005fff', title='[white]Group Details Xtracted[/white]'))
            total.append(group_name)
        end_time = time.time()
        end_resuls(end_time, start_time)

if __name__ == '__main__':
    CHmy_FILES(["config.json", "input_data.txt", "cookie.txt", ".username.txt"])
    main()