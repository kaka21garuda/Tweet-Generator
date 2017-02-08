import random

from flask import Flask, redirect, url_for, request
from gen_histogram import histogram
from sample import generate_probability, generate_word

app = Flask(__name__)


def histogram_probability(dict_histogram):
    prob_dict = {}
    sum_values = sum(dict_histogram.values())
    for k in dict_histogram.keys():
        prob_dict[k] = (float(dict_histogram[k]) / sum_values)
    # return stochastic_pick(prob_dict)
    return prob_dict


def stochastic_pick(dict_histogram):
    # getting a random float from [0.0 to 1.0)
    rand_float = random.random()
    # initialize the probability distribution
    init_probability = 0.0
    for word, prob in dict_histogram.iteritems():
        init_probability += prob
        if rand_float < init_probability:
            return word


@app.route('/')
def hello_world():
    sentence = []
    dict_histogram = histogram('tom_sawyer.txt')
    tes_dict = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    dict_prob = histogram_probability(dict_histogram)
    for i in range(17):
        sentence.append(stochastic_pick(dict_prob))
    return " ".join(sentence)


if __name__ == '__main__':
    app.run(debug=True)
    # print stochastic_pick()
