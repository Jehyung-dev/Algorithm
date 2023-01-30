# 벌집

import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input().rstrip())   # N 입력 받기
num = 1 # 벌집 범위의 최대값
cnt = 0 # 몇 칸 걸리는지 카운트
if N==1:    # 1인경우는 그냥 1
    output('1')
else:   # 아닌 경우는 N이 작을 때까지 반복루프
    while num < N:
        num+=6*cnt
        cnt+=1
    output(f'{cnt}')