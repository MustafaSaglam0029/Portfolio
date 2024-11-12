def short_words(string):
    word_list = string.split()
    len_of_words = []
    for word in word_list:
            len_of_words.append(len(word))
    lowest_len = len_of_words[0]
    for i in len_of_words:
        if len_of_words[1] < lowest_len:
            lowest_len = len_of_words[1]
    return lowest_len
print(short_words("looking far away over the hill"))
#do it without min and you can do it in one line of code.