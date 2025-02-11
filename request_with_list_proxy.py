import requests

with open("Lightning_Proxies.txt") as f:
    proxies = [line.strip() for line in f if line.strip()]

TARGET_URL = "https://api.myip.com"

with open("log_list_proxy.txt", "a") as log_file:
    for proxy in proxies:
        proxy_dict = {'https': proxy, 'http': proxy}

        for _ in range(5):
            try:
                response = requests.get(
                    TARGET_URL, proxies=proxy_dict, timeout=5)
                print(response.text)
            except Exception as e:
                print(f"Error: {e}")
            log_file.write(f"Response: {response.text}\n")
        print('*'*10)
        log_file.write("*" * 10 + "\n")
