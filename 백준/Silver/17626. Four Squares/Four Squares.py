# Four Squares


def Cnt():
    global dp

    for i in range(2, N + 1):
        Min = int(1e9)
        j = 1

        while j**2 <= i:
            Min = min(Min, dp[i - (j**2)])
            j += 1
        dp[i] = Min + 1


N = int(input())
dp = [0] * (N + 2)
dp[1] = 1

Cnt()
print(dp[N])
