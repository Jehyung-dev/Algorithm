# 숫자의 개수

import sys

ipt = sys.stdin.readline
result=1
result_list=[]
for i in range(3):  # 3개 수 입력
    result*=int(ipt().rstrip())
for j in str(result):   # 곱셈 결과를 리스트에 추가
    result_list.append(j)
for k in range(10):  # 카운트 세기
    print(result_list.count(str(k)))