# [S/W 문제해결 기본] 2일차 - Ladder1

di = [0, 0, -1]
dj = [1, -1, 0]
for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    point = 0

    for i in range(100):
        if arr[99][i] == 2:
            point = i

    i, j, dr = 99, point, 0
    visited[i][j] = True
    while i > 0:
        ni, nj = i + di[dr], j + dj[dr]
        if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1 and visited[ni][nj] == False:
            i, j = ni, nj
            visited[i][j] = True
            dr = 0
        else:
            dr = (dr + 1) % 3

    print(f'#{T} {nj}')