import random
import sys
import subprocess


def check_sys_argument():
    number = sys.argv[1]
    dictionary_words = []
    final_words = []
    # pass in the command_prompt to access the words
    proc = subprocess.Popen('tail -%s /usr/share/dict/words' % (str(number)), shell=True, stdout=subprocess.PIPE)
    # set the output of the terminal
    output = proc.communicate()[0]
    dictionary_words.append(output)
    for word in dictionary_words:
        final_words = word.split()
    # rearrange the element within the final words array
    random.shuffle(final_words)
    # return all elements to join into a sentence
    return " ".join(final_words)


if __name__ == '__main__':
    check_sys_argument()
    check = check_sys_argument()
    print check
