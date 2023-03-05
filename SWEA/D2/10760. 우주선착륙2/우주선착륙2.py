# 우주선착륙2

def is_Site():
    ans = 0
    for r in range(N):
        for c in range(M):
            cnt = 0
            for di in range(8):
                nr, nc = r + dr[di], c + dc[di]
                if 0 <= nr < N and 0 <= nc < M and arr[r][c] > arr[nr][nc]:
                    cnt += 1
            if cnt >= 4:
                ans += 1
    return ans


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t + 1} {is_Site()}')
