# 스택

import sys
input = sys.stdin.readline
output = sys.stdout.write
stack = []
cnt = -1
for _ in range(int(input().rstrip())):  # 명령어의 갯수
    temp_list = list(input().rstrip().split())   # 명령어를 임시로 받을 리스트
    if temp_list[0] == 'push':  # push는 추가
        stack.append(temp_list[1])
        cnt+=1  # 카운트를 통해 index를 구함
    elif temp_list[0] == 'pop': # 없을 경우 -1, 있다면 pop함수로 출력과 동시에 제거하며 카운트를 줄임
        if stack == []:
            output('-1' + '\n')
        else:
            output(f'{stack.pop()}' + '\n')
            cnt-=1
    elif temp_list[0] == 'size':    # 카운트 갯수 +1이 사이즈
        output(f'{cnt+1}' + '\n')
    elif temp_list[0] == 'empty':   # 빈경우 True 1, False 0
        if stack == []:
            output('1' + '\n')
        else:
            output('0' + '\n')
    else:   # top 명령어, 다른 작업없이 제일 최근 항목 출력
        if stack == []:
            output('-1' + '\n')
        else:
            output(f'{stack[cnt]}' + '\n')