from flask import Flask
from gen_histogram import histogram
from sample import generate_probability, generate_word

app = Flask(__name__)

dict_histogram = histogram('tom_sawyer.txt')

@app.route('/')
def hello_world():
    return generate_word(dict_histogram)


if __name__ == '__main__':
    app.run(debug=True)
