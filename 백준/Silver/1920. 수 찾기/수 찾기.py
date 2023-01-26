# 수 찾기

import sys

ipt = sys.stdin.readline
s=''    # 문자열 변수
N = int(ipt())  # N을 입력받음
N_lst = set(map(int, ipt().split()))   # N_lst를 set자료형으로 받음
M = int(ipt())
M_lst = list(map(int,ipt().split()))

for i in M_lst: # 숫자 M이 N_list 속에 있는지 확인
    if i in N_lst:
        s+=('1\n')    # 있다면 1을 문자열에 추가
    else:
        s+=('0\n')    # 없다면 0을 문자열에 추가
print(s)    # 한번에 문자열을 출력