import logging
import time
from threading import Thread
from datetime import datetime

import worker_new
from proxy_checker import ProxyChecker
from track import Track

URL = 'http://truck.88002223460.ru/'
URL_TEST = 'https://formdesigner.ru/form/view/192081'  # test
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
PROXY_INPUT_FILE = "proxy/proxy3.txt"
PROXY_OUTPUT_FILE = "proxy/proxy4.txt"

fields_map_new = dict(
    tel="field2158966",
    number="field2158967",
    trailer="field2158968",
    surname="field2158969",
    inn="field2158970",
)

buttons_map_new = dict(
    tel="next213861",
    number="next213862",
    trailer="next213863",
    surname="next213864",
)

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

fields_map_test = dict(
    number="field2165237",
    trailer="field2165238",
    surname="field2165239",
    inn="field2165240",
)

buttons_map_test = dict(
    tel="next214212",
    number="next214929",
    trailer="next214930",
    surname="next214931",
)


def start_worker(instans_, checker_):
    # w = worker.Worker(URL_TEST, fields_map_test, buttons_map_test)
    w = worker_new.Worker(URL, fields_map_new, buttons_map_new)
    w.start(instans_, checker_)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO, filename="log/track.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")

    tracks = [
        Track("н337мт75", "ам928375", "Балданов Б.Р.", "8001018238", "7(914)444-2174", [7, 1]),
        Track("н184на75", "ам333975", "Иринчинова В.Б.", "8001018679", "7(996)313-9602", [7, 1]),
        Track("м100ое75", "ак120062", "Гармаев К.Б.", "8001018372", "7(924)800-0083", [7, 1]),
        Track("м947ус75", "ак261345", "Базаров Б.", "8001018679", "7(924)574-2400", [1]),
        Track("в852мс80", "ам433175", "ООО Альянс Авто+", "8001018936", "7(914)498-3255", [1]),
        Track("е310нх67", "ак757867", "ООО КЛС", "6713005059", "7(914)471-1298", [7]),
    ]

    date_time_str = '2023-01-26 04:59'
    # date_time_str = '2023-01-09 02:14'
    date_time_start = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
    # date_time_obj = datetime.now()
    print('Дата и время старта:', date_time_start)

    while datetime.now() < date_time_start:
        print(datetime.now())
        time.sleep(5)

    checker = ProxyChecker()

    threads = []
    for i in tracks:
        th = Thread(target=start_worker, args=(i, checker))
        th.start()
        threads.append(th)

    for t in threads:
        t.join()
