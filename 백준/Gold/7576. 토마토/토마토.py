# 토마토

from collections import deque


def BFS():
    global Q
    while Q:
        r, c = Q.popleft()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not arr[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


def Check():
    Max = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not arr[i][j]:
                return 0
            if Max < visited[i][j]:
                Max = visited[i][j]
    return Max


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited[i][j] = 1
            Q.append((i, j))

BFS()
ans = Check()

if ans:
    print(ans-1)
else:
    print(-1)
