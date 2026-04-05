# Script by @lakshycore | Channel: @LAKSHYA_LIE
import requests, random

Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
F = '\033[2;32m'  # Green
C = '\033[2;35m'  # Pink
W = "\033[1;37m"  # White

# Input Telegram details
token = os.getenv('TG_TOKEN')
chat_id = os.getenv('TG_ID')
print(W + "\n🚀 Starting fast IG 4L checker...\n")

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# Username checker
def check(username):
    try:
        res = requests.post(
            'https://www.instagram.com/accounts/web_create_ajax/attempt/',
            headers={
                'x-ig-app-id': '936619743392459',
                'user-agent': 'Mozilla/5.0',
                'x-requested-with': 'XMLHttpRequest',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'cookie': 'csrftoken=abc123xyz',
                'content-type': 'application/x-www-form-urlencoded'
            },
            data=f'email=test%40gmail.com&username={username}&first_name=&opt_into_one_tap=false'
        ).text

        if '"username_is_taken"' in res:
            print(f"{Z}[TAKEN]{X} ➝ {username}")
        elif '"username":"' in res:
            print(f"{F}[AVAILABLE]{C} ➝ {username}")
            msg = f"🔥 Available IG 4L: {username}\nBy: @lakshycore | @LAKSHYA_LIE"
            requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}')
        else:
            print(f"{Z}[BLOCKED] ➝ {username}")
    except:
        pass  # Silent fail for speed

# Fast loop
def run():
    while True:
        u = ''.join(random.choices(chars, k=4))
        check(u)

run()
