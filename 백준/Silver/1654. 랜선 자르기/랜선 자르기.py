# 랜선 자르기

import sys
input = sys.stdin.readline
output = sys.stdout.write
K, N = list(map(int, input().rstrip().split())) # K와 N 입력
lan_cable_list = [] # 랜 케이블을 받을 리스트
for _ in range(K):  # 리스트의 형태로 랜케이블을 받음
    lan_cable_list.append(int(input().rstrip()))
min_num = 1
max_num = max(lan_cable_list)


while min_num <= max_num:
    lan_number = 0
    mid = (min_num+max_num)//2
    for i in lan_cable_list:
        lan_number+=(i//mid)

    if lan_number < N:
         max_num = mid-1
    else:
        min_num = mid+1
        result = mid
output(f'{result}')