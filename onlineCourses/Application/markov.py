import random

class Markov(dict):

    def __init__(self, words_list=None):
        super(Dictogram, self).__init__()
        if words_list:
            self.link_up(words_list)

    def link_up(self, words_list):
        for i in range(0, len(words_list) - 2):
            if words_list[i] not in self:
                self[words_list[i]] = [words_list[i + 1]]
            self[words_list[i]].append(words_list[i + 1])
        return self

    def gen_sent(self):
