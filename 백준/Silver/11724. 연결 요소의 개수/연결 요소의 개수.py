# 연결 요소의 개수

from collections import deque


def BFS(n):
    global visited

    Q = deque()
    Q.append(n)
    visited[n] = 1

    while Q:
        num = Q.popleft()
        for w in graph[num]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ans = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        BFS(i)
        ans += 1

print(ans)
