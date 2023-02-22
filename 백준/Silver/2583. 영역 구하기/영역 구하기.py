# 영역 구하기

from collections import deque


def BFS(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] == 0 and visited[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1
    return cnt


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ans = []

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(M - r2, M - r1):
        for j in range(c1, c2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if not graph[i][j] and not visited[i][j]:
            ans.append(BFS(i, j))
            
ans = sorted(ans)
print(len(ans))
print(*ans)
