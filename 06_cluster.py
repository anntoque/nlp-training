input_str = ('paraparaparadise','paragraph')

def ngram(n, words):
    answer_list = []
    for index in range(0, len(words)-n+1):
        answer_list.append(words[index:index+n])
    return answer_list

list_text_x = ngram(2,input_str[0])
list_text_y = ngram(2,input_str[1])

set_x = set(list_text_x)
set_y = set(list_text_y)

print(set_x.union(set_y))
print(set_x.intersection(set_y))
print(set_x.difference(set_y))