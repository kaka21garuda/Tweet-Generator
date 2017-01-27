import random
import sys
import os

import subprocess


def check_sys_argument():
    number = int(sys.argv[1])
    dictionary_words = []
    # call_result = os.system('tail -%s /usr/share/dict/words' % (number))
    # return "RESULT: %s" % (call_result)
    # call_result = os.popen('tail -%s /usr/share/dict/words' % (number)).read()
    # return "This is call result: %s " % (call_result)
    proc = subprocess.Popen('tail -%s /usr/share/dict/words' % (str(number)),
                            shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    dictionary_words.append(output)
    for word in dictionary_words:
        return word.split()


if __name__ == '__main__':
    check_sys_argument()
    check = check_sys_argument()
    print check
