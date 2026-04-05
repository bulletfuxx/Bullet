#!/usr/bin/env python3
"""
🔥 BULLET COMBINED INSTAGRAM CHECKER 🔥
- Checks both Usernames (4L) and Emails
- Auto-finds available ones
- Sends to Telegram
- Visible CMD window for monitoring
"""

import requests
import random
import string
import time
import os
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════

class Colors:
    RED = '\033[1;31m'
    YELLOW = '\033[1;33m'
    GREEN = '\033[1;32m'
    CYAN = '\033[1;36m'
    MAGENTA = '\033[1;35m'
    WHITE = '\033[1;37m'
    RESET = '\033[0m'

# Telegram credentials (will be injected by workflow)
TG_TOKEN = os.getenv('TG_TOKEN', '')
TG_CHAT_ID = os.getenv('TG_ID', '')

# Statistics
stats = {
    'usernames_checked': 0,
    'usernames_available': 0,
    'emails_checked': 0,
    'emails_available': 0,
    'start_time': datetime.now()
}

# ═══════════════════════════════════════════════════════════
# BANNER
# ═══════════════════════════════════════════════════════════

def show_banner():
    banner = f"""
{Colors.CYAN}{'='*70}
{Colors.RED}    ██████╗ ██╗   ██╗██╗     ██╗     ███████╗████████╗
    ██╔══██╗██║   ██║██║     ██║     ██╔════╝╚══██╔══╝
    ██████╔╝██║   ██║██║     ██║     █████╗     ██║   
    ██╔══██╗██║   ██║██║     ██║     ██╔══╝     ██║   
    ██████╔╝╚██████╔╝███████╗███████╗███████╗   ██║   
    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   
{Colors.YELLOW}         🔥 COMBINED INSTAGRAM CHECKER 🔥
{Colors.CYAN}{'='*70}
{Colors.WHITE}  [+] Checks: Usernames (4L) + Emails
  [+] Mode: Auto-find available
  [+] Alerts: Telegram notifications
  [+] Speed: Optimized with delays
{Colors.CYAN}{'='*70}{Colors.RESET}
"""
    print(banner)

# ═══════════════════════════════════════════════════════════
# TELEGRAM
# ═══════════════════════════════════════════════════════════

def send_telegram(message):
    """Send notification to Telegram"""
    if not TG_TOKEN or not TG_CHAT_ID:
        return False
    
    try:
        url = f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
        data = {
            'chat_id': TG_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        requests.post(url, data=data, timeout=5)
        return True
    except:
        return False

# ═══════════════════════════════════════════════════════════
# USERNAME CHECKER (4L)
# ═══════════════════════════════════════════════════════════

def check_username(username):
    """Check if Instagram username is available"""
    try:
        headers = {
            'x-ig-app-id': '936619743392459',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'cookie': f'csrftoken={random.randbytes(16).hex()}',
            'content-type': 'application/x-www-form-urlencoded'
        }
        
        data = f'email=test{random.randint(1000,9999)}%40gmail.com&username={username}&first_name=Test&opt_into_one_tap=false'
        
        response = requests.post(
            'https://www.instagram.com/accounts/web_create_ajax/attempt/',
            headers=headers,
            data=data,
            timeout=10
        )
        
        result = response.text
        stats['usernames_checked'] += 1
        
        if '"username_is_taken"' in result or 'username is taken' in result.lower():
            print(f"{Colors.RED}[TAKEN]{Colors.YELLOW} {username}{Colors.WHITE} (#{stats['usernames_checked']}){Colors.RESET}")
            return False
        
        elif '"username":"' in result or 'username_suggestions' in result:
            print(f"\n{Colors.GREEN}{'='*70}")
            print(f"{Colors.GREEN}[🎯 AVAILABLE USERNAME!]{Colors.CYAN} {username}")
            print(f"{Colors.GREEN}{'='*70}{Colors.RESET}\n")
            
            stats['usernames_available'] += 1
            
            # Send to Telegram
            msg = f"""🔥 *AVAILABLE INSTAGRAM USERNAME* 🔥

👤 Username: `{username}`
📊 Check #: {stats['usernames_checked']}
✅ Total Found: {stats['usernames_available']}
🕐 Time: {datetime.now().strftime('%H:%M:%S')}

🤖 By: @BULLET_CHECKER_BOT"""
            
            send_telegram(msg)
            return True
        
        else:
            print(f"{Colors.MAGENTA}[BLOCKED]{Colors.WHITE} {username} (Rate limit?){Colors.RESET}")
            return None
    
    except Exception as e:
        print(f"{Colors.RED}[ERROR]{Colors.WHITE} {username}: {str(e)[:30]}{Colors.RESET}")
        return None

# ═══════════════════════════════════════════════════════════
# EMAIL CHECKER
# ═══════════════════════════════════════════════════════════

def generate_email():
    """Generate random email to check"""
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    
    # Random email patterns
    patterns = [
        # Short random
        lambda: ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(4, 6))),
        # Name-like
        lambda: ''.join(random.choices(string.ascii_lowercase, k=4)) + str(random.randint(1, 999)),
        # With dots
        lambda: ''.join(random.choices(string.ascii_lowercase, k=3)) + '.' + ''.join(random.choices(string.ascii_lowercase, k=3)),
    ]
    
    username = random.choice(patterns)()
    domain = random.choice(domains)
    
    return f"{username}@{domain}"

def check_email(email):
    """Check if email is available on Instagram"""
    try:
        headers = {
            'X-Csrftoken': random.randbytes(16).hex(),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.instagram.com/accounts/emailsignup/'
        }
        
        data = {
            'email': email,
            'username': 'test' + str(random.randint(1000, 9999)),
            'first_name': 'Test',
            'opt_into_one_tap': 'false'
        }
        
        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/check_email/',
            headers=headers,
            data=data,
            timeout=10
        )
        
        result = response.text
        stats['emails_checked'] += 1
        
        if '"valid":true' in result or '"available":true' in result:
            print(f"\n{Colors.GREEN}{'='*70}")
            print(f"{Colors.GREEN}[🎯 AVAILABLE EMAIL!]{Colors.CYAN} {email}")
            print(f"{Colors.GREEN}{'='*70}{Colors.RESET}\n")
            
            stats['emails_available'] += 1
            
            # Send to Telegram
            msg = f"""📧 *AVAILABLE INSTAGRAM EMAIL* 📧

📬 Email: `{email}`
📊 Check #: {stats['emails_checked']}
✅ Total Found: {stats['emails_available']}
🕐 Time: {datetime.now().strftime('%H:%M:%S')}

🤖 By: @BULLET_CHECKER_BOT"""
            
            send_telegram(msg)
            return True
        
        elif '"email_is_taken"' in result:
            print(f"{Colors.RED}[TAKEN]{Colors.YELLOW} {email}{Colors.WHITE} (#{stats['emails_checked']}){Colors.RESET}")
            return False
        
        else:
            print(f"{Colors.MAGENTA}[UNKNOWN]{Colors.WHITE} {email}{Colors.RESET}")
            return None
    
    except Exception as e:
        print(f"{Colors.RED}[ERROR]{Colors.WHITE} {email}: {str(e)[:30]}{Colors.RESET}")
        return None

# ═══════════════════════════════════════════════════════════
# STATISTICS
# ═══════════════════════════════════════════════════════════

def show_stats():
    """Display current statistics"""
    elapsed = (datetime.now() - stats['start_time']).total_seconds()
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    
    print(f"\n{Colors.CYAN}{'─'*70}")
    print(f"{Colors.YELLOW}📊 STATISTICS")
    print(f"{Colors.CYAN}{'─'*70}")
    print(f"{Colors.WHITE}⏱️  Runtime: {hours}h {minutes}m")
    print(f"📝 Usernames Checked: {stats['usernames_checked']} | ✅ Available: {stats['usernames_available']}")
    print(f"📧 Emails Checked: {stats['emails_checked']} | ✅ Available: {stats['emails_available']}")
    print(f"{Colors.CYAN}{'─'*70}{Colors.RESET}\n")

# ═══════════════════════════════════════════════════════════
# MAIN CHECKER
# ═══════════════════════════════════════════════════════════

def main():
    """Main checker loop"""
    show_banner()
    
    # Check Telegram connection
    if TG_TOKEN and TG_CHAT_ID:
        print(f"{Colors.GREEN}[+] Telegram: Connected{Colors.RESET}")
        send_telegram("🔥 *Bullet Checker Started!*\n\nChecking usernames and emails...")
    else:
        print(f"{Colors.YELLOW}[!] Telegram: Not configured (set TG_TOKEN and TG_ID){Colors.RESET}")
    
    print(f"{Colors.CYAN}\n{'='*70}")
    print(f"{Colors.WHITE}Starting continuous checker...{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*70}\n")
    
    chars = string.ascii_lowercase + string.digits + '_.'
    
    try:
        iteration = 0
        
        while True:
            iteration += 1
            
            # Alternate between username and email checks
            if iteration % 2 == 1:
                # Check username (4L)
                username = ''.join(random.choices(chars, k=4))
                check_username(username)
                time.sleep(random.uniform(0.5, 1.5))
            
            else:
                # Check email
                email = generate_email()
                check_email(email)
                time.sleep(random.uniform(0.8, 2.0))
            
            # Show stats every 50 checks
            if (stats['usernames_checked'] + stats['emails_checked']) % 50 == 0:
                show_stats()
    
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Stopped by user{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}[!] Fatal error: {e}{Colors.RESET}")
    finally:
        show_stats()
        print(f"{Colors.GREEN}[+] Checker stopped{Colors.RESET}\n")
        
        if TG_TOKEN and TG_CHAT_ID:
            send_telegram(f"⏸️ *Checker Stopped*\n\nUsernames: {stats['usernames_checked']} ({stats['usernames_available']} available)\nEmails: {stats['emails_checked']} ({stats['emails_available']} available)")

if __name__ == "__main__":
    main()
