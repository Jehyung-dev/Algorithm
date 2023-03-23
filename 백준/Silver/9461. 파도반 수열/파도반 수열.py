# 파도반 수열

def func(n):
    if dp[n] == 0:
        dp[n] = func(n-3) + func(n-2)

    return dp[n]


idx = []
for _ in range(int(input())):
    idx.append(int(input())-1)

dp = [0]*(max(idx)+1)
for i in range(0, 3):
    dp[i] = 1

for j in idx:
    print(func(j))
