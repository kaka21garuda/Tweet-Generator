import word_array
import random


class Mar(object):

    def __init__(self, order):
        # the amount of words to remember
        self.order = order
        self.group_size = self.order + 1
        self.text = []
        self.graph = dict()
        return

    def find_pair(self, filename):
        self.text = word_array.list_token(filename)

        for i in range(0, len(self.text) - self.group_size):

            key = tuple(self.text[i:i + self.order])
            value = self.text[i + self.order]

            if key in self.graph:
                self.graph[key].append(value)
            else:
                self.graph[key] = [value]
        return

    def gent_sentence(self, length):
        index = random.randint(0, len(self.text) - self.order)
        result = self.text[index:index + self.order]

        for i in range(length):

            current_state = tuple(result[len(result) - self.order:])
            next_state = random.choice(self.graph[current_state])
            result.append(next_state)

        return " ".join(result[self.order:])


m = Mar(order=2)
m.find_pair("sawyer.txt")
print m.gent_sentence(26)
