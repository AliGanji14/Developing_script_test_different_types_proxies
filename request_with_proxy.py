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
        print(response_one.text)

        response_second = requests.get(
            CHANGE_IP_URL, proxies=proxies, timeout=10)
        change_data = response_second.json()

        if "error_message" in change_data:
            print(change_data['error_message'])
            wait_time = change_data.get('left',15)
            print(f"Waiting {wait_time} seconds before retrying...")
            time.sleep(wait_time)
        else:
            print(change_data)
        with open("log_proxy.txt", "a") as a:
            a.write(
                f"Request_One: {response_one.text}\nRequest_Second: {response_second.text}\n")
    except Exception as e:
        print(e)
    time.sleep(5)
