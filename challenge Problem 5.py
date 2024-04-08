
def s(word_list, word, num=0):

    #Basecase
    if len(word_list) < 1:
        return 'Fail'

    #recursive statement
    if word == word_list[0]:
        print(num)
        return
    else:
        return s(word_list[1:], word, num + 1)


if __name__ == '__main__':
    words = ["Are", "Body", "Career", "Computer", "Dam", "Mathematics", "Science", "Ugh", "Why"]
    test = s(words, "Computer")
