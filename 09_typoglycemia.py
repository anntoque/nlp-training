import random

question_text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# 入力した文章にタイポグリセミアを適応
def typoglycemia(input_text):
    cipher_text_list = []
    split_text = question_text.split()
    for string in split_text:
        if len(string) < 4:
            cipher_text_list.append(string)
        else:
            first_character = string[0]
            end_character = string[-1]
            shuffle_string = ''.join(random.sample(string[1:-1], len(string[1:-1],)))
            cipher_text_list.append(first_character + shuffle_string + end_character)
    return ' '.join(cipher_text_list)

print(typoglycemia(question_text))