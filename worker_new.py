# worker_new.py

import argparse

import requests

from registration_form import RegistrationForm

TEL = "tel"
NUMBER = "number"
TRAILER = "trailer"
SURNAME = "surname"
INN = "inn"
INTERVAL = "interval"

URL = 'http://truck.88002223460.ru/'
URL_TEST = 'https://formdesigner.ru/form/view/192081'  # test

# fields_map = dict(
#     pageId="213865",
#     phone="",
#     num_truck="",
#     num_trailer="",
#     person="",
#     inn="field2157250",
#     submit="send",
# )

fields_map_test = dict(
    pageurl="https://formdesigner.ru/form/view/192081",
    pageId="214932",
    field2161804="7(123) 555-1234",
    field2165237="a123aa38",
    field2165238="Andrey",
    field2165239="12334",
    field2165240="sadf",
    submit="send",
)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--%s' % TEL, nargs='?', default=79501040000)
    parser.add_argument('--%s' % NUMBER, nargs='?', default='a234bf34')
    parser.add_argument('--%s' % TRAILER, nargs='?', default='123456')
    parser.add_argument('--%s' % SURNAME, nargs='?', default='test')
    parser.add_argument('--%s' % INN, nargs='?', default=1234567890)
    parser.add_argument('--%s' % INTERVAL, nargs='+', default=[1, 2])

    return parser


class Worker:

    def __init__(self, url, fields, buttons):
        self.url = URL
        # self.fields = fields
        # self.buttons = buttons

    def start(self, track, checker):
        fields_map = dict()
        fields_map["referrer"] = ""
        fields_map["pageId"] = "213865"
        fields_map["phone"] = track.tel
        fields_map["num_truck"] = track.number
        fields_map["num_trailer"] = track.trailer
        fields_map["person"] = track.surname
        fields_map["inn"] = track.inn
        fields_map["submit"] = "send",
        fields_map["790fb4296c0cae550b0b849bfb4949fc"] = "a0eda65aaba6390b6491dfcc794fca54702f6ed0"

        proxy = checker.get_checked_proxy()
        print("Proxy %s\n" % proxy)
        proxies = dict(http='socks5://%s' % proxy, https='socks5://%s' % proxy)

        RegistrationForm(self.url).wait_field(5)

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "application/json; charset=utf-8",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Host": "truck.88002223460.ru",
            "Origin": "http://truck.88002223460.ru/",
            "Referer": "https://88002223460.ru/"
        }

        tail_url = "http://truck.88002223460.ru/tail.php"
        # r = requests.post(uuu, headers=headers, json=fields_map)
        r = requests.post(tail_url, headers=headers, json=fields_map, proxies=proxies)
        # r = requests.post(URL_TEST + "/tail.php", headers=headers, json=fields_map_test)

        r.encoding = 'utf-8'
        print(r.status_code)
        print(r.text)
