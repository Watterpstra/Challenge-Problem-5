'''
example to be made recursively

    def s(word_list, word):
  i = 0
  while i < len(word_list):
    if word == word_list[i]:
      print(i)
      break
    elif word < word_list[i]:
      print("Fail")
      break
    else: i += 1
  if i >= len(word_list):
    print("Fail")

'''

def s(word_list, word, num):

    #Basecase
    if len(word_list) < 1:
        return 'Fail'

    #recursive statement
    if word == word_list[0]:
        return f'{word}, {num}'
    else:
        return s(word_list[1:], word, num + 1)


if __name__ == '__main__':
    words = ["Are", "Body", "Career", "Computer", "Dam", "Mathematics", "Science", "Ugh", "Why"]
    test = s(words, "Body", 0)
    print(test)