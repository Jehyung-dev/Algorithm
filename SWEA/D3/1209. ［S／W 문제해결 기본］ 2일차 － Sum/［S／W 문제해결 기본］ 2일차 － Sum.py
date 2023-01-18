# Sum

for i in range(10):
    total_sum = []
    tmp1 = 0
    tmp2 = 0
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        for k in range(100):
            tmp1 += arr[j][k]
            tmp2 += arr[k][j]
        total_sum.append(tmp1)
        total_sum.append(tmp2)
        tmp1 = 0
        tmp2 = 0

    for l in range(100):
        tmp1 += arr[l][l]
        tmp2 += arr[l][99-l]
    total_sum.append(tmp1)
    total_sum.append(tmp2)
    tmp1 = 0
    tmp2 = 0

    print(f'#{T} {max(total_sum)}')