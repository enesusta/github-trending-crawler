from bs4 import BeautifulSoup
from util import strip_new_line


def description(row):
    soup = BeautifulSoup(row, 'html.parser')
    repository_description = soup.find("p", {"class": "col-9 text-gray my-1 pr-4"})
    return strip_new_line(repository_description.text).strip()
