with open ('./hightemp.txt','r',encoding='utf-8') as file_temp:
    text = file_temp.read()

list_column1 = []
list_column2 = []

for line in text.strip().split('\n'):
    if len(line) > 0:
        list_column1.append(line.split('\t')[0])
        list_column2.append(line.split('\t')[1])

with open ('./column1.txt','a',encoding='utf-8') as file_column1:
    print(*list_column1,sep='\n',file=file_column1)

with open ('./column2.txt','a',encoding='utf-8') as file_column2:
    print(*list_column2,sep='\n',file=file_column2)