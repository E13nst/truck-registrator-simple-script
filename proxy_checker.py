import random

import requests

TEST_URL = "http://ident.me/"
VALID_STATUSES = [200]  # [200, 301, 302, 307, 404]
PROXY_TIMEOUT = 1
PROXY_INPUT_FILE = "proxy/proxy3.txt"
PROXY_OUTPUT_FILE = "proxy/proxy4.txt"


class ProxyChecker:

    def __init__(self):
        self.proxies_list = open(PROXY_INPUT_FILE, "r").read().strip().split("\n")
        self.working = set()
        self.not_working = set()

    @staticmethod
    def check_proxy(proxy):
        try:
            response = requests.get(TEST_URL, proxies={'http': f"socks5://{proxy}"}, timeout=PROXY_TIMEOUT)
            if response.status_code in VALID_STATUSES:  # valid proxy
                print(response.status_code, response.text)
                return True
        except Exception as e:
            print("Exception: ", type(e))
            return False

    def check_all_proxies(self, output_file):
        of = open(output_file, "a")

        for p in self.proxies_list:
            if self.check_proxy(p):
                print(p)
                self.working.add(p)
                of.write(p + "\n")

        of.close()
        return self.working

    def get_random_proxy(self):
        available_proxies = tuple(self.working)
        return random.choice(available_proxies)

    def get_checked_proxy(self):
        available_proxies = tuple(self.proxies_list)
        p = random.choice(available_proxies)
        if not self.check_proxy(p):
            return self.get_checked_proxy()
        else:
            return p
