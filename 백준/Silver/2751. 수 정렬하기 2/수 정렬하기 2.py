# 수 정렬하기 2
import sys

ipt=sys.stdin.readline

N = int(ipt())    # N개의 정수를 받음
lst = []    # 입력을 받을 리스트를 만듦
for i in range(N):  # N번의 반복으로 str형으로 수를 받음
    lst.append(int(ipt()))
lst.sort()  # 오름차순 정렬
for j in lst:   # 문자열을 잘라 출력
    print(j)