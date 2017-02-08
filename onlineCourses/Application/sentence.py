import sample


def generate_sentence(histogram_text):
    sentence = []
    dict_prob = sample.histogram_probability(histogram_text)
    for i in range(17):
        sentence.append(sample.stochastic_pick(dict_prob))
    return " ".join(sentence)
