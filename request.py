import requests
import urllib3

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}


def call(lang):
    request_str = f'https://github.com/trending/{lang}?since=daily&spoken_language_code=en'
    print(request_str)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page = requests.get(request_str, headers=headers, timeout=(20, 20), verify=False)
    return page.text
