# A+B - 4

import sys

ipt = sys.stdin.readline    # 입력이 끝날 때까지 가져옴
while 1:
    try:    # 예외처리 필요
        A,B=list(map(int,ipt().rstrip().split()))
        print(A+B)
    except:
        break