import random

from flask import Flask, redirect, url_for, request
from gen_histogram import histogram
from sample import generate_probability, generate_word

app = Flask(__name__)

tes_dict = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}

dict_histogram = histogram('tom_sawyer.txt')


def histogram_probability():
    prob_dict = {}
    for k in tes_dict.keys():
        prob_dict[k] = (float(tes_dict[k]) / sum(tes_dict.values()))
    # return stochastic_pick(prob_dict)
    return prob_dict


def stochastic_pick(dict_histogram):
    rand_range = random.uniform(0, 1)
    return rand_range


@app.route('/')
def hello_world():
    return "k"


if __name__ == '__main__':
    # app.run(debug=True)
    print histogram_probability()
    # print stochastic_pick()
