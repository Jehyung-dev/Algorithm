# 기찍N

import sys

ipt = sys.stdin.readline
N=int(ipt().rstrip())
for i in range(N):
    print(N-i)  # N은 그대로지만, i가 증가하며 내림차순의 형태