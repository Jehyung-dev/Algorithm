# 괄호

import sys
input = sys.stdin.readline
output = sys.stdout.write


for _ in range(int(input().rstrip())):  # 숫자만큼 반복
    string_list = [i for i in input().rstrip()] # 문자열의 원소를 리스트로 만듦
    sum = 0 # '(' = +1, ')' = -1로 계산
    error = 0   # 닫히는 괄호가 더 생길 경우, 에러 카운트
    for i in range(len(string_list)):
        if string_list[i] == '(':
            sum +=1
        else:
            sum-=1
            if sum < 0:
                error+=1
    if sum == 0 and error == 0: # 열리고 닫히는 괄호 갯수가 동일하고 에러가 없는 경우
        output('YES' + '\n')
    else:
        output('NO' + '\n')

