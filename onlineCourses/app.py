import random
import os

from flask import Flask, redirect, url_for, request
from gen_histogram import histogram
from sample import generate_probability, generate_word

app = Flask(__name__)

dict_histogram = histogram('tom_sawyer.txt')

tes_list = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]


def try_random():
    return random.choice(tes_list)


@app.route('/')
def hello_world():
    return try_random()


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = '0.0.0.0'
    app.run(debug=True, host=host, port=33507)
