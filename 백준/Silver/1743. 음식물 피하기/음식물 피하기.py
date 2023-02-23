# 음식물 피하기

from collections import deque


def BFS(i, j):
    global visited
    cnt = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        r, c = queue.popleft()
        for di in range(4):
            nr = r + dr[di]
            nc = c + dc[di]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '#' and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
    return cnt


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M, K = map(int, input().split())  # 세로, 가로, 음식물 갯수
arr = [['.'] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = []
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = '#'

for i in range(N):
    for j in range(M):
        if arr[i][j] == '#' and not visited[i][j]:
            ans.append(BFS(i, j))

print(max(ans) + 1)
