# 좌표 정렬하기 2

import sys
input = sys.stdin.readline
output = sys.stdout.write
coordinates_list = []   # 튜플을 넣을 리스트
for _ in range(int(input().rstrip())):  # 입력 숫자만큼 x,y 좌표를 받아 리스트에 추가
    x, y = map(int, input().rstrip().split())
    coordinates_list.append((x, y))
sort_coordinates_list = sorted(coordinates_list,key=lambda x: (x[1],x[0]))  # y축 , x축 순서로 오름차순
for i in range(len(coordinates_list)):
    print(sort_coordinates_list[i][0], sort_coordinates_list[i][1])