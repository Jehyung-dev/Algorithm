# 정수 제곱근

import sys
input = sys.stdin.readline
output = sys.stdout.write
n = int(input().rstrip())
min_num = 0
max_num = n
result=0

while min_num <= max_num:
    mid = (min_num+max_num)//2
    if n > mid*mid:
        min_num = mid+1
    else:
        max_num = mid-1
        result = mid
print(result)