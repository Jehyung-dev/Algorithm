# 숫자 배열 회전

def turn_90(arr, N):
    turn_arr = [[0] * N for _ in range(N)]

    for i in range(N - 1, -1, -1):
        for j in range(0, N):
            turn_arr[j][i] = arr[N - i - 1][j]
    return turn_arr


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]

    for i in range(N - 1, -1, -1):
        for j in range(0, N):
            arr_90 = turn_90(arr, N)
    for i in range(N - 1, -1, -1):
        for j in range(0, N):
            arr_180 = turn_90(arr_90, N)
    for i in range(N - 1, -1, -1):
        for j in range(0, N):
            arr_270 = turn_90(arr_180, N)

    print(f'#{t + 1}')
    for idx in range(N):
        print(''.join(map(str, arr_90[idx])), ''.join(map(str, arr_180[idx])), ''.join(map(str, arr_270[idx])))
