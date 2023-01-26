# 구구단

import sys
ipt = sys.stdin.readline
N = int(ipt().rstrip())
for i in range(1,10):   # 1부터 9까지 수룰 i에 대입
    print(f'{N} * {i} = {N*i}')