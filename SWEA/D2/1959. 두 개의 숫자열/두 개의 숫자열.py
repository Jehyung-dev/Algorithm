# 두 개의 숫자열

T = int(input())
for i in range(T):
    sli_lst = []
    result = []
    sum = 0
    N, M = map(int, input().split())
    lst_N = list(map(int,input().split()))
    lst_M = list(map(int,input().split()))

    if N <= M:
        for j in range(M-N+1):
            sli_lst = lst_M[j:j+N]
            for k in range(N):
                sum += lst_N[k]*sli_lst[k]
            result.append(sum)
            sum = 0

    else:
        for j in range(N-M+1):
            sli_lst = lst_N[j:j+M]
            for k in range(M):
                sum += lst_M[k]*sli_lst[k]
            result.append(sum)
            sum = 0

    print(f'#{i+1} {max(result)}')