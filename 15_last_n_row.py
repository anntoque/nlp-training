import argparse

parser = argparse.ArgumentParser(description='.txtの末尾からの指定行数分を出力する')
parser.add_argument('integer', metavar='N',type=int,help='表示する行数を数字で入力')
args = parser.parse_args()