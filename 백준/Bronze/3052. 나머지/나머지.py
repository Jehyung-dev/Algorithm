# 나머지

import sys

ipt = sys.stdin.readline
number_list=[ipt().rstrip() for i in range(10)] # 한줄씩 입력되는 값을 리스트로 받음
remainder_set=set(int(number_list[j])%42 for j in range(10))    # 중복을 제거하는 set사용
print(len(remainder_set))   # 나머지 값의 갯수를 출력