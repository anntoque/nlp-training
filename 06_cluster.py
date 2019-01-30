input_str = ('paraparaparadise','paragraph')

def ngram(n, words):
    answer_list = []
    for index in range(0, len(words)-n+1):
        print(index)
        print(words[index])

print(ngram(2,input_str[0]))
