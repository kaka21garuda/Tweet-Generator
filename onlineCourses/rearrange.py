import random
import sys


def random_quote():
    rand_index = random.randint(1, len(sys.argv) - 1)
    del sys.argv[0]
    # randomize all the elements in the array
    random.shuffle(sys.argv)
    return " ".join(sys.argv)



if __name__ == '__main__':
    quote = random_quote()
    print quote
