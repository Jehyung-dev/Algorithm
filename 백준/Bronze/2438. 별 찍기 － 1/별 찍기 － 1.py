# 별 찍기 - 1

import sys

ipt = sys.stdin.readline
N = int(ipt().rstrip())
for i in range(1,N+1):      # 1부터 N까지의 수를 i에 입력
    print(i*'*')