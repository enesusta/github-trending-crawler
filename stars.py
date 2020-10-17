from bs4 import BeautifulSoup


def stars_today(row):
    soup = BeautifulSoup(row, 'html.parser')
    stars_div = str(soup.find("div", {"class": "f6 text-gray mt-2"}))
    soup_child = BeautifulSoup(stars_div, 'html.parser')
    stars_span = soup_child.find("span", {"class": "d-inline-block float-sm-right"})
    return stars_span.text.strip()
