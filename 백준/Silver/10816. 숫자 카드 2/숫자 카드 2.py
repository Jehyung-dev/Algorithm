# 숫자 카드2

import sys
input = sys.stdin.readline
output = sys.stdout.write
N_dict = {}

N = int(input().rstrip())   # 숫자 카드 갯수
N_list = list(map(int,input().rstrip().split()))    # 주어진 숫자 카드 리스트
for i in N_list:    # 리스트를 기준으로 숫자 : 숫자갯수 딕셔너리를 만듦
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1

M = int(input().rstrip())   # 갯수를 구해야할 숫자 카드 갯수
M_list = list(map(int,input().rstrip().split()))    # M 숫자 리스트
for j in M_list:
    if j not in  N_dict:    # 원래 딕셔너리에 없는 수는 0으로 지정
        N_dict[j] = 0
    output(str(N_dict[j]) + ' ')