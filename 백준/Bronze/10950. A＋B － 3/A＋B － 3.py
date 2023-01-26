# A+B - 3

import sys

ipt = sys.stdin.readline
T=int(ipt().rstrip())   # 총 반복횟수
for i in range(T):  # A,B를 받고 합 출력
    A,B=list(map(int,ipt().rstrip().split()))
    print(A+B)