# 소수 구하기

import sys
input = sys.stdin.readline
output = sys.stdout.write
M, N = map(int,input().rstrip().split())    # 범위 수 입력받기
if M == 1:  # 1은 약수가 아니므로 m을 2부터 진행
    M = 2

for i in range(M, N+1): # 범위 지정
    check_prime_number = True # bool타입으로 소수인지 아닌지
    for j in range(2, int(i**(1/2))+1):  # 소수 알고리즘상 루트까지 계산하면 됨(중간값이 됨)
        if i%j==0:
            check_prime_number = False    # 나누어지면 소수 아님
            break
    else:   # 브레이크 되지 않으면 실행
        output(str(i) + '\n')