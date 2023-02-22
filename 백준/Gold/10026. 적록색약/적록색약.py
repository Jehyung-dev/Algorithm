# 적록색약

from collections import deque


def BFS(sr, sc, co):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1

    while queue:
        row, col = queue.popleft()
        for di in range(4):
            nr = row + dr[di]
            nc = col + dc[di]
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == co and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0

for c in ('R', 'G', 'B'):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == c and not visited[i][j]:
                cnt += 1
                BFS(i, j, c)
print(cnt, end=' ')

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
        visited[i][j] = 0
cnt = 0

for c in ('R', 'B'):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == c and not visited[i][j]:
                cnt += 1
                BFS(i, j, c)
print(cnt)
