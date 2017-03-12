# import dictogram
# import sample
# import sentence
# import word_array
# import word_count
import markov_chain


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    # return sample.generate_word(histogram)
    return mar.gent_sentence(26)


if __name__ == '__main__':
    mar = markov_chain.Mar(order=2)
    mar.find_pair("sawyer.txt")
    app.run(debug=True)
