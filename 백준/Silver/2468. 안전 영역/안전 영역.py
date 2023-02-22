# 안전 영역

from collections import deque


def BFS(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1

    while queue:
        r, c = queue.popleft()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] > rain and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
    return


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N = int(input())
ans = set()
graph = [list(map(int, input().split())) for _ in range(N)]
min_rain, max_rain = min(map(min, graph)) - 1, max(map(max, graph)) + 1

for rain in range(min_rain, max_rain):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] > rain and not visited[i][j]:
                cnt += 1
                BFS(i, j)
    ans.add(cnt)
print(max(ans))
