from gen_histogram import frequency, histogram
import random
import sys


def generate_word(dict_histogram):
    random_word = random.choice(dict_histogram.keys())
    print generate_probability(random_word, dict_histogram)


def generate_probability(random_word, dict_histogram):
    return "%s => %s / %s"%(random_word, frequency(random_word, dict_histogram), sum(dict_histogram.values()))


if __name__ == '__main__':

    default_histogram = histogram(sys.argv[1])
    generate_word(default_histogram)