# 점점 커지는 당근의 개수

T = int(input())
for t in range(T):
    N = int(input())
    n_list = list(map(int, input().split()))

    max = 0
    count = 1
    for i in range(N - 1):
        if n_list[i] == n_list[i + 1] - 1:
            count += 1
        else:
            if max < count:
                max = count
            count = 1
    if max < count:
        max = count
    print(f'#{t + 1} {max}')
