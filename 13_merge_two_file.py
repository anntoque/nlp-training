with open('./column1.txt','r',encoding='utf-8') as column1_tmp:
    text_column1 = column1_tmp.read()
with open('./column2.txt','r',encoding='utf-8') as column2_tmp:
    text_column2 = column2_tmp.read()

merage =''

for column1,column2 in zip(text_column1.split('\n'),text_column2.split('\n')):
    merage += column1 + '\t' + column2 + '\n'

with open('./merge.txt','a',encoding='utf-8') as file_merge:
    print(merage,file=file_merge)