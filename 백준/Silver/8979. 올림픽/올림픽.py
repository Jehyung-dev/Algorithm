# 올림픽

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if arr[i][0] == K:
        index = i
        break

for j in range(index + 1):
    if arr[j][1] == arr[index][1] and arr[j][2] == arr[index][2] and arr[j][3] == arr[index][3]:
        rank = j
print(rank)
