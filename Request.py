# My first program
import time

import requests
import urllib3
from selenium import webdriver

import Objects as myObjects

# Disabling warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Session initialization and default headers.
session = requests.Session()
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Accept-Language": "en-US;q=0.5",
    "Accept-Encoding": "gzip, deflate",
}

# start web browser
options = webdriver.ChromeOptions()
# options.add_argument("headless")
browser = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=options)


# Print status in green or red.
def print_status(status_code, url):
    class Colors:
        RED = "\033[1;31m"
        GREEN = "\033[0;32m"
        BLUE = "\033[34m"

    if status_code in [200, 201]:
        print(Colors.GREEN + str(status_code) + ' ' + url + Colors.GREEN)

    if status_code in [400, 500]:
        print(Colors.RED + str(status_code) + ' ' + url + Colors.RED)


# Perform GET or POST request.
def request(mainRequest=myObjects.RequestObject()):
    if mainRequest.method == "GET":
        response = session.get(mainRequest.url, headers=headers, verify=False)

    if mainRequest.method == "POST":
        response = session.post(mainRequest.url, data=mainRequest.post, headers=headers, verify=False)

    print_status(response.status_code, mainRequest.url)

    return mainRequest


def selenium_request(mainRequest=myObjects.RequestObject()):
    # get source code
    try:
        browser.get(mainRequest.url)
    except Exception as e:
        return 'Non-existent'
    browser.get(mainRequest.url)
    time.sleep(2)

    print_status(browser, mainRequest.url)

    return browser.page_source


def close_browser():
    # close web browser
    browser.quit()
