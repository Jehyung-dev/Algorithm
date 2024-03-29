# 1로 만들기

N = int(input())
dp = [0] * (N + 3)
dp[2] = 1
dp[3] = 1

if N > 3:
    for i in range(4, N + 1):
        if not i % 3 and not i % 2:
            dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1, dp[i - 1] + 1)
        elif not i % 3:
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
        elif not i % 2:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
        else:
            dp[i] = dp[i - 1] + 1

print(dp[N])
