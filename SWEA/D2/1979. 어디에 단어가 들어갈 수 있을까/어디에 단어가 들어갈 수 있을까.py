# 어디에 단어가 들어갈 수 있을까

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    re_arr = [[0]*N for _ in range(N)]
    arr_str = [[0] for _ in range(N)]
    re_arr_str = [[0] for _ in range(N)]
    check, count = '1'*K, 0
    for i in range(N):
        for j in range(N):
            re_arr[i][j] = arr[j][i]
    for m in range(N):
        arr_str[m] = ''.join(arr[m])
        re_arr_str[m] = ''.join(re_arr[m])
    for m in range(N):
        arr_str[m] = arr_str[m].split('0')
        re_arr_str[m] = re_arr_str[m].split('0')

    for p in range(N):
        for q in arr_str[p]:
            if q == check:
                count += 1
        for q in re_arr_str[p]:
            if q == check:
                count += 1
    print(f'#{t+1} {count}')