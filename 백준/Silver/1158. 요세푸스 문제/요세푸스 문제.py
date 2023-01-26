# 요세푸스 문제 = 요세푸스 문제0

from collections import deque       # 덱을 쓰기위한 명령어
import sys

ipt = sys.stdin.readline
N, K = list(map(int,ipt().split())) # N과 K를 만듦
queue = deque(i for i in range(1,N+1)) # 1부터 N까지의 덱을 만듦
pop_list = []
for i in range(N):
    queue.rotate(-K+1)        # 마이너스가 왼쪽으로 밀림
    pop_list.append(queue.popleft())        # 왼쪽의 것을 뽑아 리스트에 넣음
print('<',end = '')
for i in range(0,len(pop_list)-1):
    s = print(pop_list[i], end=', ')
print(pop_list[N-1], '>', sep = '')