import argparse

parser = argparse.ArgumentParser(description='.txtの末尾からの指定行数分を出力する')
parser.add_argument('integer', metavar='N',type=int,help='表示する行数を数字で入力')
args = parser.parse_args()

with open('./hightemp.txt','r',encoding='utf-8') as file_temp:
    for index,line in enumerate(reversed(file_temp.readlines())):
        print(line.strip())
        if index+1 == args.integer:
            break