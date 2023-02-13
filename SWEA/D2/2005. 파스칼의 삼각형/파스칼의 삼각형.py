# 파스칼의 삼각형

T = int(input())
for t in range(T):
    N = int(input())
    if N == 1:
        print(f'#{t + 1}\n1')
    else:
        dp = [[] for _ in range(N + 1)]
        dp[1].append(1)
        dp[2].append(1)
        dp[2].append(1)
        for i in range(3, N+1):
            dp[i].append(1)
            for j in range(i-2):
                dp[i].append(dp[i-1][j]+dp[i-1][j+1])
            dp[i].append(1)

        print(f'#{t+1}')
        for arr in range(1, N+1):
            print(*dp[arr])
