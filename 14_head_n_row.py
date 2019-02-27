import argparse

parser = argparse.ArgumentParser(description='.txtの先頭行を指定行分表示する')
parser.add_argument('integer',metavar='N',type=int,help='表示する行数を数字で入力')
args = parser.parse_args()

text = ''
with open ('./hightemp.txt','r',encoding='utf-8') as file_temp:
    for i in range(args.integer):
        text +=file_temp.readline()

print(text)