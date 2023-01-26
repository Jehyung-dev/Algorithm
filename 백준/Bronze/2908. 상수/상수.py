# 상수

import sys

ipt = sys.stdin.readline
num1, num2=list(ipt().rstrip().split())
num1=num1[::-1] # 뒤집기
num2=num2[::-1] # 뒤집기
if num1 >= num2:
    print(num1)
else:
    print(num2)