# 달팽이 숫자

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i, j, dr, count = 0, 0, 0, 1
    arr[i][j] = count
    count += 1

    while count <= N * N:
        ni, nj = i + di[dr], j + dj[dr]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = count
            count += 1
        else:
            dr = (dr + 1) % 4

    print(f'#{t+1}')
    for lst in arr:
        print(*lst)
