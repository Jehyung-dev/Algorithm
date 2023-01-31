# 균형잡힌 세상

import sys
input = sys.stdin.readline

while 1:    # 무한루프
    string = input().rstrip()   # 문자열을 받음
    if string == '.':   # .이면 멈춤
        break
    bracket_list = []   # 초기화와 괄호를 받기 위한 리스트
    err = True  # 잘못된지 아닌지 판단하는 bool형식

    for i in string:    # 스펠링을 i에 대입
        if i == '[' or i == '(':    # 열리는 괄호만 넣음
            bracket_list.append(i)
        elif i == ']':
            if not bracket_list or bracket_list[-1] == '(': # 비어있지 않거나 괄호가 반대면
                err = False # false 후 멈춤
                break
            elif bracket_list[-1] == '[':   # 괄호가 일치하면 꺼내기
                bracket_list.pop()
        elif i == ')':  # 같은 상황
            if not bracket_list or bracket_list[-1] == '[':
                err = False
                break
            elif bracket_list[-1] == '(':
                bracket_list.pop()
    if err == True and not bracket_list:    # 에러가 없거나 열리는 괄호만 있는 경우는 false이기에 빈 리스트 조건 추가
        print('yes')
    else:
        print('no')