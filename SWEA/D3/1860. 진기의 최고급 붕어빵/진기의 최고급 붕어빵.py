# 진기의 최고급 붕어빵

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    stock = (arr[-1] + 1) * [0]
    isBuy = 1
    for i in range(arr[-1] + 1):
        stock[i] = i // M * K

    for time in arr:
        for i in range(time, arr[-1] + 1):
            stock[i] -= 1
            if stock[i] < 0:
                isBuy = 0
                break
    if isBuy:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
