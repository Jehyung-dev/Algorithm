def start_spot(arr, H, W):
    for r in range(H):
        for c in range(W):
            if arr[r][c] == '^' or arr[r][c] == 'v' or arr[r][c] == '<' or arr[r][c] == '>':
                return (r, c)

def Up(arr, r, c, cmd):
    nr = r + dx[dir[cmd]]
    nc = c + dy[dir[cmd]]
    if 0 <= nr and arr[nr][nc] == '.' and arr[nr][nc] != '-':
        arr[r][c], arr[nr][nc] = '.', '^'
        return (arr, nr, nc)
    else:
        arr[r][c] = '^'
        return (arr, r, c)


def Down(arr, r, c, cmd):
    nr = r + dx[dir[cmd]]
    nc = c + dy[dir[cmd]]
    if nr < H and arr[nr][nc] == '.' and arr[nr][nc] != '-':
        arr[r][c], arr[nr][nc] = '.', 'v'
        return (arr, nr, nc)
    else:
        arr[r][c] = 'v'
        return (arr, r, c)


def Left(arr, r, c, cmd):
    nr = r + dx[dir[cmd]]
    nc = c + dy[dir[cmd]]
    if 0 <= nc and arr[nr][nc] == '.' and arr[nr][nc] != '-':
        arr[r][c], arr[nr][nc] = '.', '<'
        return (arr, nr, nc)
    else:
        arr[r][c] = '<'
        return (arr, r, c)


def Right(arr, r, c, cmd):
    nr = r + dx[dir[cmd]]
    nc = c + dy[dir[cmd]]
    if nc < W and arr[nr][nc] == '.' and arr[nr][nc] != '-':
        arr[r][c], arr[nr][nc] = '.', '>'
        return (arr, nr, nc)
    else:
        arr[r][c] = '>'
        return (arr, r, c)


def Shoot(arr, r, c):
    if arr[r][c] == '^':
        for i in range(r - 1, -1, -1):
            if arr[i][c] == '*':
                arr[i][c] = '.'
                return arr
            elif arr[i][c] == '#':
                return arr
        else:
            return arr
    elif arr[r][c] == 'v':
        for i in range(r + 1, H):
            if arr[i][c] == '*':
                arr[i][c] = '.'
                return arr
            elif arr[i][c] == '#':
                return arr
        else:
            return arr
    elif arr[r][c] == '<':
        for j in range(c - 1, -1, -1):
            if arr[r][j] == '*':
                arr[r][j] = '.'
                return arr
            elif arr[r][j] == '#':
                return arr
        else:
            return arr
    else:
        for j in range(c + 1, W):
            if arr[r][j] == '*':
                arr[r][j] = '.'
                return arr
            elif arr[r][j] == '#':
                return arr
        else:
            return arr


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    cmds = input()
    r, c = start_spot(arr, H, W)

    for cmd in cmds:
        if cmd == 'U':
            arr, r, c = Up(arr, r, c, cmd)
        elif cmd == 'D':
            arr, r, c = Down(arr, r, c, cmd)
        elif cmd == 'L':
            arr, r, c = Left(arr, r, c, cmd)
        elif cmd == 'R':
            arr, r, c = Right(arr, r, c, cmd)
        else:
            arr = Shoot(arr, r, c)

    print(f'#{t + 1} ', end='')
    for i in arr:
        print(f"{''.join(i)}")