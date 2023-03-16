# 프린터 큐

from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    Q = deque()
    for i in list(map(int, input().split())):
        Q.append(i)
    cnt = 1

    while 1:
        if M == 0 and max(Q) == Q[M]:
            break
        elif max(Q) == Q[0]:
            Q.popleft()
            cnt += 1
        else:
            Q.rotate(-1)

        if M == 0:
            M = len(Q)-1
        else:
            M -= 1

    print(cnt)
