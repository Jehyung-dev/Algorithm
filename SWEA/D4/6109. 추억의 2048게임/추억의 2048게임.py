# 추억의 2048게임

def set_arr(temp_arr, N, dr):
    if dr == 'up':
        arr = [[0]*N for _ in range(N)]
        for r in range(N):
            idx = 0
            for c in range(N):
                if temp_arr[c][r] != 0:
                    arr[idx][r] = temp_arr[c][r]
                    idx += 1
        return arr
    if dr == 'down':
        arr = [[0]*N for _ in range(N)]
        for r in range(N):
            idx = N-1
            for c in range(N-1, -1, -1):
                if temp_arr[c][r] != 0:
                    arr[idx][r] = temp_arr[c][r]
                    idx -= 1
        return arr
    if dr == 'left':
        arr = [[0]*N for _ in range(N)]
        for r in range(N):
            idx = 0
            for c in range(N):
                if temp_arr[r][c] != 0:
                    arr[r][idx] = temp_arr[r][c]
                    idx += 1
        return arr
    if dr == 'right':
        arr = [[0]*N for _ in range(N)]
        for r in range(N):
            idx = N-1
            for c in range(N-1, -1, -1):
                if temp_arr[r][c] != 0:
                    arr[r][idx] = temp_arr[r][c]
                    idx -= 1
        return arr
def move_up(arr, N):
    for c in range(N):
        for r in range(N-1):
            if arr[r][c] != 0 and arr[r][c] == arr[r+1][c]:
                arr[r][c] *= 2
                arr[r+1][c] = 0
    return arr
def move_down(arr, N):
    for c in range(N):
        for r in range(N-1,0,-1):
            if arr[r][c] != 0 and arr[r][c] == arr[r-1][c]:
                arr[r][c] *= 2
                arr[r-1][c] = 0
    return arr
def move_left(arr, N):
    for r in range(N):
        for c in range(N-1):
            if arr[r][c] != 0 and arr[r][c] == arr[r][c+1]:
                arr[r][c] *= 2
                arr[r][c+1] = 0
    return arr
def move_right(arr, N):
    for r in range(N):
        for c in range(N-1, 0, -1):
            if arr[r][c] != 0 and arr[r][c] == arr[r][c-1]:
                arr[r][c] *= 2
                arr[r][c-1] = 0
    return arr

T = int(input())
for t in range(T):
    N, direction = input().split()
    N = int(N)
    temp_arr = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0] * N for _ in range(N)]
    index = f'#{t+1}'

    if direction == 'up':
        arr = set_arr(temp_arr, N, direction)
        arr = move_up(arr, N)
        arr = set_arr(arr, N, direction)
    elif direction == 'down':
        arr = set_arr(temp_arr, N, direction)
        arr = move_down(arr, N)
        arr = set_arr(arr, N, direction)
    elif direction == 'left':
        arr = set_arr(temp_arr, N, direction)
        arr = move_left(arr, N)
        arr = set_arr(arr, N, direction)
    else:
        arr = set_arr(temp_arr, N, direction)
        arr = move_right(arr, N)
        arr = set_arr(arr, N, direction)

    print(index)
    for i in arr:
        print(*i)