# 수 정렬하기 3

import sys

input = sys.stdin.readline
number_list = [0 for q in range(10001)]
N=int(input())
for _ in range(N):
    number_list[int(input())]+=1
for j in range(10001):
    if number_list[j] != 0:
        for i in range(number_list[j]):
            print(j)