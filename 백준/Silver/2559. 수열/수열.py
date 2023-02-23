# 수열

N, K = map(int, input().split())
arr = list(map(int, input().split()))
j = sum = 0

for i in range(0, K):
    sum += arr[i]
ans = sum

while j < N - K:
    sum = sum - arr[j] + arr[j + K]
    if sum > ans:
        ans = sum
    j += 1

print(ans)
