from bs4 import BeautifulSoup
from util import strip


def owner(row):
    soup = BeautifulSoup(row, 'html.parser')
    repository_owner = str(soup.find("h1", {"class": "h3 lh-condensed"}))
    repository = 'https://github.com/' + strip(extract_repository_name(repository_owner))
    data = {'repository': repository}
    return data


def extract_owner_name(owner_str):
    soup = BeautifulSoup(owner_str, 'html.parser')
    owner_name = soup.find("span", {"class": "text-normal"})
    return owner_name.text.strip()


def extract_repository_name(owner_str):
    soup = BeautifulSoup(owner_str, 'html.parser')
    repository_name = soup.findAll("a")[0]
    return repository_name.text.strip()
