import random

question_text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# スペースで区切られた単語列に対して
# 各単語の先頭と末尾の文字は残し
# それ以外はランダムに並び替える

def typoglycemia(input_text):
    cipher_text = "" 
    split_text = print(question_text.split())
    for string in split_text:
        if len(string) < 4:
            return
        else:
            first_character = string[0]
            end_character = string[-1]
            shuffle_string = ''.join(random.sample(string[1:-1], len(string)))

            return first_character + shuffle_string + end_character
        