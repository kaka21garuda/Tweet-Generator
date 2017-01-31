import sys


# this function takes in string file and returns
#  the number of number of words that appear in a format of dictionary
def histogram(source_text):
    words_array = []
    # lists of all different words
    number_different_words = 0
    dictionary = {}
    with open(source_text, 'r') as myfile:
        # read the data file and remove all unnecessary characters
        data = myfile.read().replace('\n', ' ').replace('(', '').replace(')', '').replace('"','').lower()
        # split the data from sentences to words.
        words_array = data.split()
    for word in words_array:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    # returns a data structure in a format of dictionary
    return dictionary


def unique_words(dict_histogram):
    # returns the total count of unique words in the histogram
    unique_words_set = dict_histogram.keys()
    return len(unique_words_set)


def cool_words(dict_histogram):
    # THE MOST FREQUENT WORD
    most_used_word = max(dict_histogram, key=dict_histogram.get)
    # THE LEAST WORDS IN THE TEXT, THAT ONLY CAME OUT ONCE
    least_words = [k for k, v in dict_histogram.iteritems() if v == 1]
    print most_used_word
    print least_words


def frequency(word, dict_histogram):
    if word in dict_histogram:
        return dict_histogram[word]
    else:
        return 0

# def test():
#     lst = []
#     for i in range(100):
#         lst.append(i)

if __name__ == '__main__':

    default_histogram = histogram(sys.argv[1])
    print unique_words(default_histogram)
    # print unique_words(histogram('paul_blog.txt'))
    # print timeit.timeit("test()", setup="from __main__ import test")
