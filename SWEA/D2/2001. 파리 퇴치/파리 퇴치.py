# 파리 퇴치

def add_square(arr, start, end):
    sum = 0
    for i in range(M):
        for j in range(M):
            sum += arr[start+i][end+j]
    return sum

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            if add_square(arr, i, j) > max:
                max = add_square(arr, i, j)
    print(f'#{t+1} {max}')