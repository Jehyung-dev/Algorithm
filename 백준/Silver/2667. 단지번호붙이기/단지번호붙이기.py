# 단지번호붙이기

from collections import deque


def BFS(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()
        for di in range(4):
            nr = r + dr[di]
            nc = c + dc[di]
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == '1' and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
    return cnt


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N = int(input())
graph = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == 0:
            ans.append(BFS(i, j))

ans = sorted(ans)
print(len(ans), *ans, sep='\n')
