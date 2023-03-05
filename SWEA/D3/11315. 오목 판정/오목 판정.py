# 오목 판정

def is_Five():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for di in range(4):
                    nr, nc = r, c
                    for _ in range(4):
                        cnt = 0
                        nr, nc = nr + dr[di], nc + dc[di]
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                            cnt += 1
                        else:
                            break
                    else:
                        return 'YES'
    return 'NO'


dr = [0, 1, 1, 1]
dc = [1, 0, -1, 1]
for t in range(int(input())):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{t + 1} {is_Five()}')
