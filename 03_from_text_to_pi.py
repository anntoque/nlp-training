import re

# HACK: 同じ引数に連続して何度も代入しているので可読性が低い。もう少しまとめたい
input_text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
input_text = input_text.replace('.',"")
input_text = input_text.replace(',',"")
input_text = input_text.split()

answer_list = []

for value in input_text:
    answer_list.append(len(value))

print(answer_list)
