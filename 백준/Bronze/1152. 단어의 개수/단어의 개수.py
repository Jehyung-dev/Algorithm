# 단어의 개수

import sys

ipt = sys.stdin.readline
string=ipt().rstrip().strip()   # 좌우 공백 제거
word_list=list(string.split())    # 단어 리스트
print(len(word_list))