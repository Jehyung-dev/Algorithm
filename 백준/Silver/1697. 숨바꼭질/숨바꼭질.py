# 숨바꼭질

from collections import deque


def BFS(q):
    tmp = []
    while q:
        num = q.popleft()
        if 0 <= num <= 100000 and not visited[num]:
            visited[num] = 1
            if num == K:
                return 0
            tmp += [num - 1, num + 1, num * 2]
    return tmp


visited = [0] * 100001
N, K = map(int, input().split())
Q = deque([N - 1, N + 1, N * 2])
cnt = 0

if N == K:
    print(cnt)
else:
    while 1:
        result = BFS(Q)
        cnt += 1
        if not result:
            print(cnt)
            break
        else:
            Q = deque(result)
