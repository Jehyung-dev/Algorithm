# 큐

from collections import deque 
import sys
input = sys.stdin.readline
output = sys.stdout.write
queue = deque() # 큐 설정

for _ in range(int(input().rstrip())):  # 명령어의 갯수
    temp_list = list(input().rstrip().split())   # 명령어를 임시로 받을 리스트
    if temp_list[0] == 'push':  # push는 추가
        queue.append(temp_list[1])
    elif temp_list[0] == 'pop': # 없을 경우 -1, 있다면 왼쪽 출력과 동시에 제거
        if queue == deque([]):
            output('-1' + '\n')
        else:
            output(f'{queue.popleft()}' + '\n')
    elif temp_list[0] == 'size':    # 큐의 길이로 사이즈 출력
        output(f'{len(queue)}' + '\n')
    elif temp_list[0] == 'empty':   # 빈경우 True 1, False 0
        if queue == deque([]):
            output('1' + '\n')
        else:
            output('0' + '\n')
    elif temp_list[0] == 'front':   # 처음 항을 출력
        if queue == deque([]):
            output('-1' + '\n')
        else:
            output(f'{queue[0]}' + '\n')
    elif temp_list[0] == 'back':   # -1을 통해 마지막 항 출력
        if queue == deque([]):
            output('-1' + '\n')
        else:
            output(f'{queue[-1]}' + '\n')