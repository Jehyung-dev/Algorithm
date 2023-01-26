# 별 찍기 - 2

import sys

ipt = sys.stdin.readline
N=ipt().rstrip()    # 별 갯수 받기
for i in range(1,int(N)+1): # 1부터 N까지 받기
    print(' '*(int(N)-i),i*'*',sep='')