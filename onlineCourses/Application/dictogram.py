class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of unique words/distinct items in dictionary
        self.tokens = 0  # the total of all tokens in the dictionary
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for word in iterable:
            if word not in self:
                self[word] = 1
            self[word] += 1
        # returns a data structure in a format of dictionary
        return self

    def unique_words(self):
        """Return the amount of different words in the histogram"""
        self.types = len(self.keys())
        return self.types

    def frequency(self, word):
        """Return the count of the given item in this histogram, or 0"""
        # return the count of the word,
        # if the word not in dictogram, return 0
        return self.get(word, 0)
