# 블랙잭

import sys
input = sys.stdin.readline
output = sys.stdout.write
N, M = map(int, input().rstrip().split())   # N과 M을 대입받음
card_list=list(map(int,input().rstrip().split()))   # 카드 리스트를 받음
card_list.sort()    # 소팅
min = 999999    # min값을 넣을 변수

for i in range(0, N-2): # 3가지를 더하는 모든 경우의 수
    for j in range(i+1, N-1):
        for k in range(j+1,N):
            sum = card_list[i]+card_list[j] +card_list[k]   # 카드 3개의 합
            if M-sum < min and M-sum >=0:   # 0이상이고 차이가 최소인 경우 min에 대입
                min = M-sum
output(f'{M-min}')