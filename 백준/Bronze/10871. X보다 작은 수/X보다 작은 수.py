# X보다 작은 수

import sys

ipt = sys.stdin.readline
N, X=list(map(int,ipt().rstrip().split()))   # N과 X입력
under_x=[]  # X보다 작은 수를 넣을 리스트
A=list(map(int,ipt().rstrip().split())) # 수열 입력
for j in A: # x보다 작은 수 입력
    if j < X:
        under_x.append(j)
for k in range(len(under_x)-1):   # 출력
    print(under_x[k], end=" ")
print(under_x[len(under_x)-1])