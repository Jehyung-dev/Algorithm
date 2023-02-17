# 우주선착륙2

def Check(r,c):
    global result
    cnt = 0
    for di in range(8):
        nr = r + dr[di]
        nc = c + dc[di]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        else:
            if arr[nr][nc] < arr[r][c]:
                cnt+=1
        if cnt >= 4:
            result += 1
            break


dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            Check(i,j)
    print(f'#{t+1} {result}')