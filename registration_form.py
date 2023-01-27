import logging
import time
import requests
from bs4 import BeautifulSoup


class RegistrationForm:

    def __init__(self, url):
        self.url = url
        self.tel_field = None
        self.html = self.get_html()

    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            logging.info(result.text)
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_tel_field(self):
        self.html = self.get_html()
        soup = BeautifulSoup(self.html, 'html.parser')

        self.tel_field = soup.find('input', type='tel')
        print(self.tel_field)
        return self.tel_field

    def check_field(self):
        return self.get_tel_field() is not None

    def wait_field(self, seconds):
        while not self.check_field():
            print("sleep %s seconds" % seconds)
            time.sleep(seconds)



