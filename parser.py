import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_source_html(url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)

        source_code = driver.page_source

    except Exception as _ex:
        print(_ex)

    finally:
        return source_code
        driver.close()
        driver.quit()


def items_urls(source_code):
    mass = []
    mass1 = []

    soup = BeautifulSoup(source_code, 'lxml')
    item_divs = soup.findAll("div", class_="data_med_block_first")
    for item in item_divs:
        item_url = item.find("div", class_="data_med_name").find("a")
        mass1.append(item_url.get('href'))
        mass1.append(item_url.text)
        mass.append(mass1)
        mass1 = []

    return mass


def items_urls1(source_code):
    mass = []
    mass1 = []

    soup = BeautifulSoup(source_code, 'lxml')
    item_divs = soup.find("div", class_="top20_comp").findAll("a")
    print(item_divs)
    for item in item_divs:
        mass1.append(item.get('href'))
        mass1.append(item.text)
        mass.append(mass1)
        mass1 = []

    return mass


def main(name):
    return items_urls(get_source_html(url=f"https://pillintrip.com/advanced_search?query={name}"))


def main1(url):
    get_source_html(url)
    return items_urls1(get_source_html(url))

# import json
# import requests

# from google.protobuf.json_format import MessageToJson
# from proto_structs import offers_pb2


# def parse_page(name='нурофен'):
    # """
    # :param city: location of the shop
    # :param shop: shop name
    # :param page_num: parsed page number
    # :return: None
    # """
    # url = f"https://api.pillintrip.com/advanced_search?&limit=20&lang=en&query={name}"
    # data = requests.get(url, allow_redirects=True)  # data.content is a protobuf message
    # print(data)
    # offers = offers_pb2.Offers()  # protobuf structure
    # offers.ParseFromString(data.content)  # parse binary data
    # products: str = MessageToJson(offers)  # convert protobuf message to json
    # products = json.loads(products)
    # print(json.dumps(products, indent=4, ensure_ascii=False,))


# if __name__ == "__main__":
#     parse_page()


# import requests


# def fetch(url, params):
#     url = f"https://api.pillintrip.com/advanced_search?&limit=1000&lang=en&query=%D0%BD%D1%83%D1%80%D0%BE%D1%84%D0%B5%D0%BD"
#     headers = params['headers']
#     if params['method'] == 'GET':
#         pills = requests.get(url, headers=headers)
#     elif params['method'] == 'POST':
#         pills = requests.post(url, headers=headers)
#
#     print(pills.status_code)
#     print(pills.json()['medicines'])
#     for i in pills.json()['medicines']:
#         print(i['name'], i['slug'])
#
#     return 0

# name = 'Нурофен'
# fetch(name, {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"macOS\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "Referer": "https://pillintrip.com/",
#     "Referrer-Policy": "strict-origin-when-cross-origin"
#   },
#   "body": None,
#   "method": "GET"
# });


# def fetch1(url, params):
#     headers = params['headers']
#     if params['method'] == 'GET':
#         pills = requests.get(url, headers=headers)
#     elif params['method'] == 'POST':
#         pills = requests.post(url, headers=headers)
#
#     print(pills.status_code)
#
#
# fetch1("https://pillintrip.com/search_analog_ru-nurofen_in_thailand", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "content-type": "text/plain;charset=UTF-8",
#     "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"macOS\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "Referer": "https://pillintrip.com/",
#     "Referrer-Policy": "strict-origin-when-cross-origin"
#   },
#   "body": "{\"api_key\":\"HJjhs634kjhreifus8234602ngfshdl;kkf72634jwslo4jkdhf\",\"state\":\"main_search\",\"url_medicine\":\"ru-nurofen\",\"url_target_country\":\"thailand\",\"language\":\"en\"}",
#   "method": "POST"
# });