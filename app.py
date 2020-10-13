from flask import Flask, request
from bs4 import BeautifulSoup
from request import call

app = Flask(__name__)


@app.route('/')
def index():
    lang = request.args.get('lang')
    response = call(lang)
    soup = BeautifulSoup(response, 'html5lib')

    return f'Param is {lang}'
