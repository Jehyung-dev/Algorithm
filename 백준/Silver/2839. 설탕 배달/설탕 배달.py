# 설탕 배달

import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input().rstrip())   # 배달 설탕 무게
min_num = set() # 봉지 갯수를 넣을 세트

if N%5==0:  # set에 5로 나누어지는 경우, 3으로 나눠지는경우 몫을 넣음
    min_num.add(N//5)
elif N%3==0:
    min_num.add(N//3)

for i in range(1,N//5+1):   # 5를 차례로 줄여가며 동시에 3으로 나눠지는 경우가 있는지 파악
    N-=5
    if N%3==0:
        min_num.add(N//3 + i)

if min_num == set():    #   모든 경우가 없다면 -1출력
    output('-1')
else:   # 나누어지는 세트 중 최소 갯수만 출력
    output(f'{min(min_num)}')