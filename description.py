from bs4 import BeautifulSoup
from util import strip_new_line


def description(row):
    soup = BeautifulSoup(row, 'html.parser')
    repository_description = soup.find("p", {"class": "col-9 color-text-secondary my-1 pr-4"})
    print(repository_description)
    if repository_description is not None:
        return strip_new_line(repository_description.get_text()).strip()
    else:
        return ""
