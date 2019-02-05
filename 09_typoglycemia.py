import random

question_text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# TODO: シャッフル処理は実装したので、文字列をリストで開始、空白区切りで結合する処理を実装
# 入力した文章にタイポグリセミアを適応

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
        