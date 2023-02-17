# 재미있는 오셀로 게임

def Start(arr, N):
    for i in range(2):
        arr[N // 2 + i - 1][N // 2 + i - 1] = 'W'
        arr[N // 2 + i - 1][N // 2 - i] = 'B'
    return arr


def Play(arr, r, c, color):
    if color == 1:
        arr[r][c] = 'B'
        for dir in range(8):
            nr = r + dr[dir]
            nc = c + dc[dir]
            temp = []
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'W':
                    temp.append([nr, nc])
                elif arr[nr][nc] == 'B' and temp != []:
                    for point in temp:
                        arr[point[0]][point[1]] = 'B'
                    break
                else:
                    break
                nr += dr[dir]
                nc += + dc[dir]


    else:
        arr[r][c] = 'W'
        for dir in range(8):
            nr = r + dr[dir]
            nc = c + dc[dir]
            temp = []
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 'B':
                    temp.append([nr, nc])
                elif arr[nr][nc] == 'W' and temp != []:
                    for point in temp:
                        arr[point[0]][point[1]] = 'W'
                    break
                else:
                    break
                nr += dr[dir]
                nc += + dc[dir]
    return arr


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr = Start(arr, N)
    B = W = 0
    for _ in range(M):
        r, c, color = map(int, input().split())
        arr = Play(arr, r - 1, c - 1, color)
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'B':
                B += 1
            elif arr[r][c] == 'W':
                W += 1
    print(f'#{t + 1} {B} {W}')
