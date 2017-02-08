import random

import sample
import sentence
import tokenize
import word_count


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    list_tokens = tokenize.list_token("tom_sawyer.txt")
    histogram = word_count.generate_histograms(list_tokens)
    # return sample.generate_word(histogram)
    return sentence.generate_sentence(histogram)


if __name__ == '__main__':
    app.run()
