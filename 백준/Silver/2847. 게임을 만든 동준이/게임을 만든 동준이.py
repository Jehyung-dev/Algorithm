# 게임을 만든 동준이

N = int(input())
arr = [0] * N
sum = 0
for i in range(N):
    arr[i] = int(input())

for j in range(N - 1, 0, -1):
    if arr[j - 1] >= arr[j]:
        sum += arr[j - 1] - arr[j] + 1
        arr[j - 1] = arr[j] - 1
print(sum)
