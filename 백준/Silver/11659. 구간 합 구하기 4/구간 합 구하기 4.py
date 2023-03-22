# 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
sum = [0]
temp = 0

for i in arr:
    temp += i
    sum.append(temp)

for _ in range(M):
    ans = 0
    s, e = map(int, input().rstrip().split())

    print(sum[e]-sum[s-1])
