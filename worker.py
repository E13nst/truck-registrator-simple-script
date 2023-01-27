# worker.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from registration_form import RegistrationForm
from proxy_checker import ProxyChecker
from track import Track

import argparse
import capcha

TEL = "tel"
NUMBER = "number"
TRAILER = "trailer"
SURNAME = "surname"
INN = "inn"
INTERVAL = "interval"

# URL = 'https://formdesigner.ru/form/view/191827'
# URL_TEST = 'https://formdesigner.ru/form/view/192081'  # test

intervals = {
    7: '2023-01-13 04:57',
    1: '2023-01-13 04:17',
}

# fields_map = dict(
#     tel="field2157250",
#     number="field2157251",
#     trailer="field2157253",
#     surname="field2157255",
#     inn="field2157257",
# )
#
# buttons_map = dict(
#     tel="next213674",
#     number="next213675",
#     trailer="next213676",
#     surname="next213677",
# )
#
# fields_map_test = dict(
#     number="field2165237",
#     trailer="field2165238",
#     surname="field2165239",
#     inn="field2165240",
# )
#
# buttons_map_test = dict(
#     tel="next214212",
#     number="next214929",
#     trailer="next214930",
#     surname="next214931",
# )


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
        self.url = url
        self.fields = fields
        self.buttons = buttons

    def get_digit(self, table):
        lines = list()
        for tr in table:
            tds = tr.find_elements(By.TAG_NAME, "td")
            line = 0
            for td in tds:
                line = line << 1
                if td.get_attribute('class'):
                    line = line | 1
            lines.append(line)
            # print(" OR: %s" % bin(line))
        return lines

    def start(self, track, checker):

        for n in range(0, 500):
            try:
                proxy = checker.get_checked_proxy()
                print("Proxy %s\n" % proxy)

                options = Options()
                options.add_argument('--proxy-server=socks5://%s' % proxy)
                options.accept_insecure_certs = True
                # options.add_argument("--headless")

                driver = webdriver.Chrome(options=options)
                driver.get(self.url)

                RegistrationForm(self.url).wait_field(5)

                for num in range(0, 500):
                    try:
                        driver.refresh()
                        print("Try {}\n".format(track.number))

                        page_source = driver.page_source
                        of = open("./log/%s-start-new.html" % track.number, "w")
                        of.write(page_source)
                        of.close()

                        driver.find_element(By.XPATH, "//div/input[@type='tel']").send_keys(track.tel)
                        driver.find_element(By.ID, self.buttons[TEL]).click()

                        driver.find_element(By.ID, self.fields[NUMBER]).send_keys(track.number)
                        driver.find_element(By.ID, self.buttons[NUMBER]).click()

                        driver.find_element(By.ID, self.fields[TRAILER]).send_keys(track.trailer)
                        driver.find_element(By.ID, self.buttons[TRAILER]).click()

                        driver.find_element(By.ID, self.fields[SURNAME]).send_keys(track.surname)
                        driver.find_element(By.ID, self.buttons[SURNAME]).click()

                        driver.find_element(By.ID, self.fields[INN]).send_keys(track.inn)

                    except Exception as e:
                        print("Exception: ", type(e))
                        continue
                    break

                # a = 0
                # b = 0
                # op = True

                # for num in range(0, 50):
                #     try:
                #         digit1 = driver.find_elements(By.XPATH, "//div/table[1]/tbody/tr")
                #         digit2 = driver.find_elements(By.XPATH, "//div/table[2]/tbody/tr")
                #         digit3 = driver.find_elements(By.XPATH, "//div/table[3]/tbody/tr")
                #
                #         a = capcha.decode(self.get_digit(digit1))
                #         op = capcha.operation(self.get_digit(digit2))
                #         b = capcha.decode(self.get_digit(digit3))
                #
                #     except Exception as e:
                #         print("Exception: ", type(e))
                #         continue
                #     break
                #
                # result = driver.find_element(By.XPATH, "//div/input[@name='captcha']")
                # result.send_keys("%i" % capcha.calculate(a, b, op))
                #
                # driver.find_elements(By.XPATH, "//div/button[@type='submit']").pop().click()

                time.sleep(120)

                driver.save_screenshot("./log/%s-5.png" % track.number)

                page_source = driver.page_source
                of = open("./log/%s.html" % track.number, "w")
                of.write(page_source)
                of.close()

                try:
                    success_element = driver.find_element(By.XPATH,
                                                          "//div[@class='success_message success_message-top']/p")
                    print("{} {}\n".format(track.number, success_element.text))

                except Exception as e:
                    print("{} FAIL\n".format(track.number))
                    print("Exception: ", type(e))
                    driver.quit()

                driver.quit()

            except Exception as e:
                print("Exception: ", type(e))
                continue
            break

# if __name__ == '__main__':
#     parser = createParser()
#     args = parser.parse_args()
#     print(args.tel)
#     print(args.number)
#     print(args.trailer)
#     print(args.surname)
#     print(args.inn)
#     print(args.interval)
#
#     tr = Track(args.number, args.trailer, args.surname, args.inn, args.tel, args.interval)
#
#     proxy_checker = ProxyChecker()
#
#     w = Worker(URL_TEST, fields_map_test, buttons_map_test)
#     # w = Worker(URL, fields_map, buttons_map)
#
#     w.start(tr, proxy_checker)
#
#     exit(0)
