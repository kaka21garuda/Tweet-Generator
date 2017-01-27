import statistics

# this function takes in string file and returns
#  the number of number of words that appear in a format of dictionary
def histogram(source_text):
    words_array = []
    count = {}

    with open(source_text, 'r') as myfile:
        data = myfile.read().replace('\n', '').replace('.', '').replace(',', '')
        # split the data from sentences to words.
        words_array = data.split()
    for word in words_array:
        # check if the word already exists
        if word in count:
            # if yes, increment the value by 1
            count[word] += 1
        else:
            count[word] = 1
    # returns dictionary
    return count


def uniqe_words(dict_histogram):
    # most used word with value of
    most_used_number = 0
    # list of all different words
    all_words = []
    # the lists of the least that was used in the text.
    least_words = []
    value_array = []
    for key, value in dict_histogram.iteritems():
        all_words.append(key)
        # only gets the uniqe value/the least word used in the text from the histogram
        if value == 1:
            # these are the least words
            least_words.append(key)
        else:
            value_array.append(value)
            value_array = sorted(value_array, key=int)
            most_used_number = value_array[len(value_array) - 1]
    return len(least_words)


def frequency(word, dict_histogram):
    values = []
    # returns how many times does the word appear in the text.
    for key, value in dict_histogram.iteritems():
        values.append(value)
    mean = statistics.mean(values)
    median = statistics.median(values)
    return dict_histogram[word]


if __name__ == '__main__':
    # print frequency('a', histogram('paul_blog.txt'))
    print uniqe_words(histogram('paul_blog.txt'))
