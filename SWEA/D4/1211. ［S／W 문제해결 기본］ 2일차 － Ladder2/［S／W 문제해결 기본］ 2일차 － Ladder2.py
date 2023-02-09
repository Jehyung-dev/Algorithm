# [S/W 문제해결 기본] 2일차 - Ladder2
 
dr = [0, 0, 1]
dc = [1, -1, 0]
for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start = []
    min, minIdx = 9999, 0
    for point in range(100):
        if arr[0][point] == 1:
            start.append(point)
 
    for i in start:
        visited = [[False] * 100 for _ in range(100)]
        r, c, d, count = 0, i, 0, 0
        visited[r][c] = True
        while r < 99:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] == 1 and visited[nr][nc] == False:
                r, c = nr, nc
                visited[r][c] = True
                d = 0
                count += 1
            else:
                d = (d + 1) % 3
        if count < min:
            min = count
            minIdx = i
    print(f'#{T} {minIdx}')