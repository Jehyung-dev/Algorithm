# 동전 0

N, K = map(int, input().split())
arr = []
cnt, idx = 0, N-1
for _ in range(N):
    arr.append(int(input()))

while K != 0:
    if arr[idx] <= K:
        K -= arr[idx]
        cnt += 1
    else:
        idx -= 1

print(cnt)
