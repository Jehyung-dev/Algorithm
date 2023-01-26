# 나이순 정렬

import sys

ipt = sys.stdin.readline    # 빠른 입력
lst = []    # 임의 리스트 변수
indx = 0
N = int(ipt())    # 데이터 갯수 입력
for i in range(N):  # 리스트 형태로 나이 이름을 추가
    lst.append(list(ipt().rstrip().split()))
    # lst[i].append(indx) # 추가된 인덱스를 새로 추가
    # indx+=1
lst.sort(key = lambda x : (int(x[0]))) # 나이만을 기준으로 소팅
for j in lst:   # 출력
    print(f'{j[0]} {j[1]}')