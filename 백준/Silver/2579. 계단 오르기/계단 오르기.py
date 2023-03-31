# 계단 오르기


def Climb(n):
    global dp

    if n == 1:
        print(arr[1])
    elif n == 2:
        print(arr[1] + arr[2])

    else:
        dp[1] = arr[1]
        dp[2] = arr[1] + arr[2]

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])

        print(dp[n])


arr = [0]
N = int(input())
for _ in range(N):
    arr.append(int(input()))
dp = [0] * (N + 1)

Climb(N)
