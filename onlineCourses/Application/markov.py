import random

import word_array
import dictogram
import sample

class Markov(dict):

    def __init__(self, words_list=None):
        super(Markov, self).__init__()
        self.words_list = word_array.list_token("tom_sawyer.txt")
        self.hist_freq = dictogram.Dictogram(words_list)
        if words_list:
            self.link_up(words_list)

    def link_up(self, words_list):
        for i in range(0, len(words_list) - 2):
            if words_list[i] not in self:
                self[words_list[i]] = [words_list[i + 1]]
            self[words_list[i]].append(words_list[i + 1])
        return self

    def gen_sent(self):
        arr = []
        curr_state = sample.generate_word(self.hist_freq)

        for i in range(50):
            hist_next = dictogram.Dictogram(self[curr_state])
            next_choice = sample.generate_word(hist_next)
            curr_state = next_choice
            arr.append(next_choice)
        #     pick_next = random.choice(self[curr_state])
        #     arr.append(pick_next)
        return " ".join(arr)


lists = word_array.list_token("tom_sawyer.txt")
mar = Markov(words_list=lists)
print mar.gen_sent()
