import dictogram
import sample
import sentence
import word_array
import word_count


from flask import Flask


app = Flask(__name__)
# app.debug = True


@app.route('/')
def hello_world():
    # return sample.generate_word(histogram)
    return sentence.generate_sentence(histogram)


if __name__ == '__main__':
    words_list = word_array.list_token("tom_sawyer.txt")
    # make a Dictogram object which types dictionary
    histogram = dictogram.Dictogram(words_list)
    # print histogram.frequency("jkdl")
    app.run(debug=True)
