# 미로탐색

from collections import deque


def BFS(sr, sc):
    global visited

    Q = deque([(sr, sc)])
    visited[sr][sc] = 1

    while Q:
        r, c = Q.popleft()
        if r == N - 1 and c == M - 1:
            return

        for di in range(4):
            nr = r + dr[di]
            nc = c + dc[di]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

BFS(0, 0)
print(visited[N - 1][M - 1])
