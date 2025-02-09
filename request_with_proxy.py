from dotenv import load_dotenv
import os
import requests
import time


PROXY = os.getenv('PROXY')
TARGET_URL = "https://api.myip.com"
CHANGE_IP_URL = os.getenv('CHANGE_IP_URL')

proxies = {'https': PROXY, 'http': PROXY}

request_count = 0 

while True:
    try:
        response = requests.get(TARGET_URL, proxies=proxies, timeout=10)
        print(response.text)

        with open("log_proxy.txt", "a") as log_file:
            log_file.write(f"Response: {response.text}\n")

        request_count += 1

        if request_count >= 10:
            change_response = requests.get(CHANGE_IP_URL, proxies=proxies, timeout=10)
            print(f"Change IP response: {change_response.text}")

            with open("log_proxy.txt", "a") as log_file:
                log_file.write(f"Change IP Response: {change_response.text}\n")

            request_count = 0

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)
