input_text = "I am an NLPer"

# N-gramの実装
def ngram(n, words):
    answer_list = []
    for index in range(0,len(words)-n+1):
        answer_list.append(words[index:index+n])
    return answer_list

# bi-gramを出力
print(ngram(2,input_text.split(' ')))
print(ngram(2,input_text))