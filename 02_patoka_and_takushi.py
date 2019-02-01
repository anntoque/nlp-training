str_patoka = "パトカー"
str_takushi = "タクシー"
str_union = ''

# 2つのテキストの各先頭文字から、交互に文字列を結合する
for first_str, second_str in zip(str_patoka,str_takushi):
    str_union = str_union + first_str + second_str

print(str_union)

# そのほかの方法
print(''.join([a + b for a,b in zip(str_patoka,str_takushi)]))