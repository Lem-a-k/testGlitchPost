from requests import get, post
from flask import Flask, jsonify

app = Flask(__name__)

HOST = '127.0.0.1'
PORT = 8080
THIS = f'{HOST}:{PORT}'
SITE = "https://charm-shine-kilogram.glitch.me/"


@app.route('/')
def index():
    return f""" {THIS}/get to test get-request
{THIS}/post to test post-request"""


@app.route('/get')
def get_test():
    get_all = get(f'{SITE}/api/news').json()
    n_id = 1
    get_one = get(f'{SITE}/api/news/{n_id}').json()
    return jsonify([get_all, get_one])


@app.route('/post')
def post_test():
    print(post(f'{SITE}/api/news',
               json={'title': 'Header from testing',
                     'content': 'News text from testing',
                     'user_id': 1,
                     'is_private': False}).text)
    return 'OK'


if __name__ == '__main__':
    app.run(port=PORT, host=HOST)
