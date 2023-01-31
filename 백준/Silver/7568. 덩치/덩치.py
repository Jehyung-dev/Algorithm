# 덩치

import sys
input = sys.stdin.readline
build_list = [] # 키, 몸무게를 받을 리스트
rank = ''   # 최종 출력을 위한 랭킹 변수
for _ in range(int(input().rstrip())):  # 튜플 형식으로 키와 몸무게를 추가
    weight, height = map(int,input().rstrip().split())
    build_list.append((weight,height))
for i in build_list:    # 키와 몸무게 둘 다 큰 사람을 카운트
    count = 1   # 자신도 포함되어 기본 등수 1
    for j in range(0, len(build_list)):
        if i[0] < build_list[j][0] and i[1] < build_list[j][1]:
            count += 1
    rank += str(count) + ' '    # 문자열로 이어 한번에 출력
print(rank)