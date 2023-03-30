# 2×n 타일링 2


def tile(n):
    global dp

    if n == 1:
        dp[n] = 1
    elif n == 2:
        dp[n] = 3
    elif dp[n] == 0:
        dp[n] = tile(n - 2) * 2 + tile(n - 1)

    return dp[n]


n = int(input())
dp = [0] * (n + 2)

print(f"{tile(n)%10007}")
