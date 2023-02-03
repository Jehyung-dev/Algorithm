# 삼성시의 버스 노선

T = int(input())
for t in range(T):
    N = int(input())
    A = [0]*N
    for i in range(N):
        A[i] = list(map(int, input().split()))
    P = int(input())
    c_list = [0]*P
    result = [0]*P
    for j in range(P):
        c_list[j] = int(input())

    for k in range(len(c_list)):
        for l in range(N):
            if A[l][0] <= c_list[k] <= A[l][1]:
                result[k] += 1

    print(f'#{t+1}', end=' ')
    print(*result)