# 치즈

from collections import deque


def BFS():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * w for _ in range(h)]
    visited[0][0] = 1
    cnt = 0

    while queue:
        r, c = queue.popleft()
        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                if not arr[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                else:
                    arr[nr][nc] = 0
                    visited[nr][nc] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
visited = null_arr = [[0] * w for _ in range(h)]
ans, num = [], 0

while 1:
    num += 1
    cnt = BFS()
    if not cnt:
        break

print(f'{num - 1}\n{ans[-2]}')
