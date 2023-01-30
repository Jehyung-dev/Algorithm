# 분해합

import sys
input = sys.stdin.readline
output = sys.stdout.write
N = int(input().rstrip())   # 분해합 받기
check=0  # 생성자가 있는지 확인
start = N-len(str(N))*9
if start < 0:
    start = 0
else:
    start = N-len(str(N))*9
for i in range(start,N+1):  # 분해합을 기준으로 생성자의 범위 설정
    sum=0   # 자릿수를 더할 변수
    for j in str(i):    # 자릿수 더하기
        sum+=int(j)
    if sum+i == N:  # 자릿수의 합과 자기자신의 합이 분해자와 같은 경우
        output(f'{i}')
        check+=1
        break    # 생성자로 추가

if check == 0:  # 생성자가 없을 때는 0출력
    output('0')