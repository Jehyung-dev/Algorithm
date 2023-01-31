# 카드2
from collections import deque

queue = deque() # 덱을 만듦
for i in range(1,int(input())+1):
    queue.append(i)  # 1부터 N까지 카드 나열

while len(queue)!=1:    # 덱에 1개가 남을 때까지 반복
    queue.popleft() # 제일 왼쪽 카드를 버리고
    queue.rotate(-1)    # 뒤로 옮기고

print(queue[0]) # 마지막 카드를 출력