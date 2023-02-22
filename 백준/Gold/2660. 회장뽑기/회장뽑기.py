# 회장뽑기

from collections import deque


def BFS(p):
    queue = deque()
    visited = [-1] * (N + 1)
    visited[p] = 0
    queue.append(p)

    while queue:
        friend = queue.popleft()
        for temp in g[friend]:
            if visited[temp] == -1:
                queue.append(temp)
                visited[temp] = visited[friend] + 1
    return max(visited)


N = int(input())
g = [[] for _ in range(N + 1)]
Min = int(1e9)
while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    g[a].append(b)
    g[b].append(a)

for i in range(1, N+1):
    if BFS(i) < Min:
        Min = BFS(i)
        ans = [i]
    elif Min == BFS(i):
        ans.append(i)

print(Min, len(ans))
print(*ans)
