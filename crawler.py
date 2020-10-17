from flask import jsonify

from description import description
from owner import owner
from stars import stars_today


def crawl(divs):
    repos = []

    for div in divs:
        rows = div.find_all("article", class_="Box-row")
        for row in rows:
            row_str = str(row)
            object = owner(row_str)
            desc = description(row_str)
            stars = stars_today(row_str)
            object['description'] = desc
            object['stars'] = stars
            repos.append(object)

    repos = [dict(t) for t in {tuple(sorted(repo.items())) for repo in repos}]
    repos.sort(key=lambda repo: int(repo['stars'].split(' ')[0]), reverse=True)
    return jsonify(repos)
