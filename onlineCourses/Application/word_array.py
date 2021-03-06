import dictogram
import re
import random

def list_token(source_text):
    words_array = []
    # lists of all different words

    with open(source_text, 'r') as myfile:
        # read the data file and remove all unnecessary characters
        data = myfile.read().replace('\n', ' ')
        # split the data from sentences to words.
        line = re.sub(r"[^A-Za-z\s]", "", data.strip()).lower()
        words_array = line.split()
    return words_array


def iterate(list_text):
    graph = {}
    for n in range(0, len(list_text) - 2):
        if list_text[n] not in graph:
            graph[list_text[n]] = [list_text[n + 1]]
        graph[list_text[n]].append(list_text[n + 1])
    return graph


def prob_graph(word):
    prob = dictogram.Dictogram(word)
    return prob
