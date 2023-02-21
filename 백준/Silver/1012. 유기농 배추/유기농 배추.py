# 유기농 배추

def DFS(r, c):
    v[r][c] = 1
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        if g[nr][nc] and not v[nr][nc]:
            DFS(nr, nc)


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    g = [[0] * (M + 2) for _ in range(N + 2)]
    v = [[0] * (M + 2) for _ in range(N + 2)]
    ans = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        g[Y + 1][X + 1] = 1

    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if g[r][c] and not v[r][c]:
                DFS(r, c)
                ans += 1
    print(ans)
