# 좌표 정렬하기

import sys

ipt = sys.stdin.readline
lst = []
N = int(ipt())
for i in range(N):
    lst.append(list(map(int,ipt().split())))
lst.sort(key = lambda x : (x[0],x[1]))
for j in lst:
    print(f'{j[0]} {j[1]}')
