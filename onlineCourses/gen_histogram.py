import statistics


# this function takes in string file and returns
#  the number of number of words that appear in a format of dictionary
def histogram(source_text):
    words_array = []
    # lists of all different words
    number_different_words = 0

    with open(source_text, 'r') as myfile:
        # read the data file and remove all unnecessary characters
        data = myfile.read().replace('\n', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '')
        # split the data from sentences to words.
        words_array = data.split()
    # HOW MANY DIFFERENT WORDS ARE USED?
    number_different_words = len(set(words_array))
    # returns a data structure in a format of dictionary
    return {k: words_array.count(k) for k in set(words_array)}


def unique_words(dict_histogram):
    # THE MOST FREQUENT WORD
    most_used_word = max(dict_histogram, key=dict_histogram.get)
    # THE LEAST WORDS IN THE TEXT, THAT ONLY CAME OUT ONCE
    least_words = [k for k, v in dict_histogram.iteritems() if v == 1]
    # returns the total count of uniqe words in the histogram
    return len(least_words)


def frequency(word, dict_histogram):
    return dict_histogram[word]

def test():
    lst = []
    for i in range(100):
        lst.append(i)

if __name__ == '__main__':
    import timeit
    # print unique_words(histogram('paul_blog.txt'))
    print timeit.timeit("test()", setup="from __main__ import test")