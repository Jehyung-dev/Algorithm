# 직사각형에서 탈출

import sys

ipt=sys.stdin.readline
x,y,w,h=list(map(int,ipt().rstrip().split()))   # 변수 값 입력
len_list=[]
len_list.append(x)
len_list.append(y)
len_list.append(abs(x-w))   # 차이의 절댓값
len_list.append(abs(y-h))
print(min(len_list))    # 최소 길이 출력