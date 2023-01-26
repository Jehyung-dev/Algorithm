# 알파벳 찾기

import sys
ipt = sys.stdin.readline
S=list(ipt().rstrip())
result=[]   # 위치 값을 위한 리스트
for i in range(97,123): # 아스키 코드 사용
    if chr(i) not in S: # 없으면 -1을 리스트에 추가
        result.append(-1)
    else:
        result.append(S.index(chr(i)))  # 있다면 인덱스 추가
for j in range(len(result)-1):
    print(result[j], end=' ')
print(result[len(result)-1])