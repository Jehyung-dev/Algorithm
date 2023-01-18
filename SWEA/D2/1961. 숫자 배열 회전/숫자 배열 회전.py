# 숫자 배열 회전

T = int(input())
for i in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr_90 = [[] for _ in range(N)]
    arr_180 = [[] for _ in range(N)]
    arr_270 = [[] for _ in range(N)]
    
    for j in range(0, N):
        for k in range(-N+1, 1):
            arr_90[j].append(arr[abs(k)][j])

    for j in range(0, N):
        for k in range(-N+1, 1):
            arr_180[j].append(arr_90[abs(k)][j])

    for j in range(0, N):
        for k in range(-N+1, 1):
            arr_270[j].append(arr_180[abs(k)][j])
    
    print(f'#{i+1}')
    for l in range(N):
        tmp1 = arr_90[l]
        tmp2 = arr_180[l]
        tmp3 = arr_270[l]
        print(''.join(map(str,tmp1)), ''.join(map(str,tmp2)), ''.join(map(str,tmp3)))

# 2차원 리스트 join이 안됨 / join시 map으로 str형태를 만들어야함