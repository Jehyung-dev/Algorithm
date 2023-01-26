# A+B - 5

import sys

ipt = sys.stdin.readline
while 1:    # 무한루프
    A,B=list(map(int,ipt().rstrip().split()))
    if A==B==0: # 0,0이 들어오면 종료
        break
    else:
        print(A+B)