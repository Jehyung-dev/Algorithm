# 음계

import sys

ipt = sys.stdin.readline
sequence=list(map(int,ipt().rstrip().split()))   # 연주 순서의 변수
if sequence==[1,2,3,4,5,6,7,8]: # 오름차순
    print('ascending')
elif sequence==[8,7,6,5,4,3,2,1]:   # 내림차순
    print('descending')
else:
    print('mixed')