import dictogram
import sample
import sentence
import tokenize
import word_count


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    # return sample.generate_word(histogram)
    return sentence.generate_sentence(histogram.histogram())


if __name__ == '__main__':
    # make a Dictogram object which types dictionary
    histogram = dictogram.Dictogram(source_text="tom_sawyer.txt")
    app.run()
