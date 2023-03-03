# 보물섬

from collections import deque


def BFS(sr, sc):
    Q = deque()
    visited = [[0] * w for _ in range(h)]
    visited[sr][sc] = 1
    Q.append((sr, sc))

    while Q:
        r, c = Q.popleft()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and arr[nr][nc] == 'L':
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
    return visited[r][c]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
h, w = map(int, input().split())
arr = [input() for _ in range(h)]
ans = set()

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            ans.add(BFS(i, j))

print(max(ans) - 1)
