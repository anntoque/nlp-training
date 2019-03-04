import argparse
import os

parser = argparse.ArgumentParser(description='指定の行数ごとにファイルを分割する')
parser.add_argument('each_row', metavar='N', type=int, help='何行ごとに分割するかを指定')
args = parser.parse_args()

row_num = 0
cut_num = 0

with open('./hightemp.txt','r',encoding='utf-8') as file_temp:
    for index,line in enumerate(file_temp.readlines()):
        write_file_path = './question16/hightemp_cut_' + str(cut_num) +'.txt'

        if row_num == args.each_row:
            row_num = 0 
            cut_num += 1
        else:
            if os.path.isfile(write_file_path):
                with open(write_file_path,'a',encoding='utf-8') as write_file:
                    write_file.writelines(line)
            else:
                with open(write_file_path,'x',encoding='utf-8') as write_file:
                    write_file.writelines(line)
            row_num += 1
