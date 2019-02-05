question_text = "I am the bone of my sword. Steel is my body, and fire is my blood."

# 半角英字のみアトバシュ暗号化を行う
# HACK: ret += が複数回出ているのでまとめれそう
def cipher(input_text):
    ret = ""
    for character in input_text:
        if character.islower():
            ret += chr(219-ord(character))
        else:
            ret += character
    return ret

cipher_text = cipher(question_text)
decryption_text = cipher(cipher_text)

print(cipher_text)
print(decryption_text)

