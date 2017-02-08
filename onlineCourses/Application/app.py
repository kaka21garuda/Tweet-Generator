import random

import sample
import sentence

from flask import Flask


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
    return sample.generate_word("tom_sawyer.txt")
    # return sentence.generate_sentence("tom_sawyer.txt")


if __name__ == '__main__':
    app.run()
    # print stochastic_pick()
