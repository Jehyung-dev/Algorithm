# 최댓값

import sys

ipt = sys.stdin.readline
number_list=[]  # 추가할 숫자 리스트
for i in range(9):
    number_list.append(int(ipt().rstrip()))  # 한줄씩 주어지는 숫자 추가, 문자열이 아닌 숫자 중요
print(max(number_list)) # 최대값
print(number_list.index(max(number_list))+1)    # 최대값의 순서