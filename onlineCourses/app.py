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
    return stochastic_pick(prob_dict)


def stochastic_pick(dict_histogram):
    # getting a random float from 0.0 to 1.0
    rand_range = random.uniform(0, 1)
    init_probability = 0.0
    for k, v in dict_histogram.iteritems():
        init_probability += v
        if rand_range < init_probability:
            break
    return k


@app.route('/')
def hello_world():
    return histogram_probability()


if __name__ == '__main__':
    app.run(debug=True)
    # print stochastic_pick()
