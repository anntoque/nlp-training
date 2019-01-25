str_patoka = "パトカー"
str_takushi = "タクシー"
str_union = ''

for first_str, second_str in zip(str_patoka,str_takushi):
    str_union = str_union + first_str + second_str

print(str_union)

# other method
print(''.join([a + b for a,b in zip(str_patoka,str_takushi)]))