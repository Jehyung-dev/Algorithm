# 두 수 비교하기

import sys

ipt = sys.stdin.readline
A, B = list(map(int,ipt().rstrip().split()))    # A, B입력
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')