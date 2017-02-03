import random

from flask import Flask
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
    app.run(debug=True)
