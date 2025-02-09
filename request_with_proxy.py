from dotenv import load_dotenv
import os
import requests
import time


PROXY = os.getenv('PROXY')
TARGET_URL = os.getenv('TARGET_URL')
CHANGE_IP_URL = os.getenv('CHANGE_IP_URL')

proxies = {'https': PROXY, 'http': PROXY}

while True:
    try:
        response_one = requests.get(TARGET_URL, proxies=proxies, timeout=10)
        response_second = requests.get(
            CHANGE_IP_URL, proxies=proxies, timeout=10)
        print(response_one.text)
        print(response_second.text)
        with open("log_proxy.txt", "a") as a:
            a.write(
                f"Request_One: {response_one.text}\nRequest_Second: {response_second.text}\n")
    except Exception as e:
        print(e)
    time.sleep(3)
