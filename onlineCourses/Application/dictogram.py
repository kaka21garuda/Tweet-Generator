class Dictogram(dict):

    def __init__(self, source_text):
        super(Dictogram, self).__init__()
        self.source_text = source_text
        self.types = 0  # the number of unique words/distinct items in dictionary
        self.tokens = 0  # the total of all tokens in the dictionary
        if source_text:
            self.histogram()

    def histogram(self):
        words_array = []
        # lists of all different words
        with open(self.source_text, 'r') as myfile:
            # read the data file and remove all unnecessary characters
            data = myfile.read().replace('\n', ' ').replace('(', '').replace(')', '').replace('"','').lower()
            # split the data from sentences to words.
            words_array = data.split()
        for word in words_array:
            if word not in self:
                self[word] = 1
            self[word] += 1
        # returns a data structure in a format of dictionary
        return self

    def unique_words(self):
        self.types = len(self.keys())
        return self.types

    def frequency(self, word):
        return self.get(word)
