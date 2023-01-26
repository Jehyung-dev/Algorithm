# 숫자의 합

import sys

ipt = sys.stdin.readline
N=int(ipt().rstrip())   # 숫자의 갯수
numbers=ipt().rstrip()  # N개의 숫자열
sum=0   # 합을 구하기 위한 변수
for i in numbers:   # 문자열의 숫자를 하나씩 합함
    sum+=int(i)
print(sum)