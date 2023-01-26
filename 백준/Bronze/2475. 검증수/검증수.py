# 검증수

import sys
ipt = sys.stdin.readline
number = list(map(int,ipt().rstrip().split()))  # 입력값으로 리스트를 만듦
square_sum = 0  # 제곱한 값의 합을 넣을 변수
for i in number:
    square_sum+=i**2    # 5자리의 제곱을 더하는 반복문
print(square_sum%10)