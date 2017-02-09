def list_token(source_text):
    words_array = []
    # lists of all different words
    number_different_words = 0
    dictionary = {}
    with open(source_text, 'r') as myfile:
        # read the data file and remove all unnecessary characters
        data = myfile.read().replace('\n', ' ').replace('(', '').replace(')', '').replace('"','').lower()
        # split the data from sentences to words.
        words_array = data.split()
    return words_array


print list_token("tom_sawyer.txt")
