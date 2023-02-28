# 의석이의 세로로 말해요

T = int(input())
for t in range(1, T + 1):
    arr = [input() for _ in range(5)]
    max_len, s = 0, ''

    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    for j in range(max_len):
        for k in range(5):
            if j < len(arr[k]):
                s += arr[k][j]
    print(f'#{t} {s}')
