# 풍선팡

def Pop():
    ans = 0
    for r in range(N):
        for c in range(M):
            temp = arr[r][c]
            for di in range(4):
                nr, nc = r, c
                for _ in range(arr[r][c]):
                    nr, nc = nr + dr[di], nc + dc[di]
                    if 0 <= nr < N and 0 <= nc < M:
                        temp += arr[nr][nc]
            if temp > ans:
                ans = temp

    return ans


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t + 1} {Pop()}')
