# 슈퍼마리오

import sys
input = sys.stdin.readline
mushroom_list = []  # 버섯 점수 리스트
sum=0   # 점수의 합 계산

for _ in range(10): # 입력값 10개로 리스트 생성
    mushroom_list.append(int(input().rstrip()))
for i in mushroom_list: # 버섯의 점수를 합산
    sum+=i
    if sum > 100:   # 100이 넘는 순간 멈춤
        break
if 100-(sum-i)>= sum-100:   # 100전과 후를 비교 / 100이 안된다면 후자가 더 큼
    print(sum)
elif 100-(sum-i) < sum-100:
    print(sum-i)