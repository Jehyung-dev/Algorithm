# 농작물 수확하기

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    mid = (N - 1) // 2
    up, down = mid - 1, mid + 1
    i = 1
    ans = sum(map(int, arr[mid]))

    while up != -1:
        ans += sum(map(int, arr[up][i:N - i])) + sum(map(int, arr[down][i:N - i]))
        i += 1
        down += 1
        up -= 1
    print(f'#{t} {ans}')
