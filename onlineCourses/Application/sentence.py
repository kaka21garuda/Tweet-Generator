import sample

from gen_histogram import histogram


def generate_sentence(source_text):
    sentence = []
    dict_hist = histogram(source_text)
    dict_prob = sample.histogram_probability(dict_hist)
    for i in range(17):
        sentence.append(sample.stochastic_pick(dict_prob))
    return " ".join(sentence)
