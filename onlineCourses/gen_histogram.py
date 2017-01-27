import random

# this function takes in string file and returns
#  the number of number of words that appear in a format of dictionary
def histogram(source_text):
    words_array = []
    count = {}
    # uniqe_words = []
    with open(source_text, 'r') as myfile:
        data = myfile.read().replace('\n', '').replace('.', '').replace(',', '')
        words_array = data.split()
    for word in words_array:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    # return a histogram in a format of dictionary.
    return count
    # for word in words_array:
    #     if word not in uniqe_words:
    #         uniqe_words.append(word)
    # return uniqe_words


def uniqe_words(dict_histogram):


def frequency(word, histogram):
    



if __name__ == '__main__':
    # histogram = histogram('paul_blog.txt')
    # print histogram
