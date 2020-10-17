from flask import Flask, request
from bs4 import BeautifulSoup
from crawler import crawl
from request import call

app = Flask(__name__)


@app.route('/')
def index():
    lang = request.args.get('lang')
    if lang is None:
        lang = "java"
    response = call(lang)
    soup = BeautifulSoup(response, 'html5lib')
    divs = soup.find_all("div")
    return crawl(divs)
