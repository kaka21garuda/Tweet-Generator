import random

from gen_histogram import histogram


def generate_word(source_text):
    dict_histogram = histogram(source_text)
    dict_prob = histogram_probability(dict_histogram)
    return stochastic_pick(dict_prob)


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
