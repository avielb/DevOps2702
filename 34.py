import datetime
from time import sleep
import requests
def check_if_url_up(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        return True


def print_name(name):
    print(name)


print(check_if_url_up("https://github.com"))
