# import tokenize
#
#
# def generate_histograms(list_tokens):
#     hist_tokens = {}
#     for word in list_tokens:
#         if word not in hist_tokens:
#             hist_tokens[word] = 1
#         hist_tokens[word] += 1
#     return hist_tokens
#
# print generate_histograms(tokenize.list_token("tom_sawyer.txt"))
