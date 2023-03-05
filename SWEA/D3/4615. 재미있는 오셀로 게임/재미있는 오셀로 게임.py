# 재미있는 오셀로 게임

def Set_up():
    global arr
    for r, c, color in start[N]:
        arr[r][c] = color


def Play(r, c, color, Opp_color):
    global arr
    arr[r][c] = color
    for di in range(8):
        nr, nc = r + dr[di], c + dc[di]
        temp = set()
        while 1:
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == Opp_color:
                temp.add((nr, nc))
                nr, nc = nr + dr[di], nc + dc[di]
            elif 0 > nr or nr >= N or 0 > nc or nc >= N or not arr[nr][nc]:
                break
            else:
                for i, j in temp:
                    arr[i][j] = color
                break


def Cnt():
    global B, W
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                B += 1
            elif arr[i][j] == 2:
                W += 1


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
start = {
    4: [(1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 2, 2)],
    6: [(2, 2, 2), (2, 3, 1), (3, 2, 1), (3, 3, 2)],
    8: [(3, 3, 2), (3, 4, 1), (4, 3, 1), (4, 4, 2)]
}
for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    B = W = 0
    Set_up()

    for _ in range(M):
        sc, sr, color = map(int, input().split())
        if color == 1:
            Opp_color = 2
        else:
            Opp_color = 1
        Play(sr - 1, sc - 1, color, Opp_color)

    Cnt()
    print(f'#{t + 1} {B} {W}')
