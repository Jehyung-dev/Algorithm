# 제로

import sys
input = sys.stdin.readline
output = sys.stdout.write
num_list = []   # 수를 넣을 리스트

for _ in range(int(input().rstrip())):  # 첫 줄의 수만큼 반복
    num = int(input().rstrip()) # 0인지 아닌지 체크하기 위해 숫자 받기
    if num == 0: num_list.pop() # 0이면 먼저 제거
    else: num_list.append(num)  # 아닐경우 숫자 리스트에 추가
output(f'{sum(num_list)}')  # 합하기