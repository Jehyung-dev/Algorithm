# 어디에 단어가 들어갈 수 있을까

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    re_arr = [[0] * N for _ in range(N)]
    check, count = '1' * K, 0
    for i in range(N):
        for j in range(N):
            re_arr[i][j] = arr[j][i]
    for j in range(N):
        arr[j] = ''.join(arr[j]).split('0')
        re_arr[j] = ''.join(re_arr[j]).split('0')

    for p in range(N):
        for q in arr[p]:
            if q == check:
                count += 1
        for q in re_arr[p]:
            if q == check:
                count += 1
    print(f'#{t + 1} {count}')