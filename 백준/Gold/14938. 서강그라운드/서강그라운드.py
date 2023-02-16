# 서강그라운드

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
INF = int(1e9)
arr = [[INF]*n for _ in range(n)]
temp = 0
result = []

for i in range(n):
    arr[i][i] = 0

for _ in range(r):
    a,b,l = map(int, input().split())
    if arr[a - 1][b - 1] > l:
        arr[a - 1][b - 1] = l
        arr[b-1][a-1] = l


for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] <= m:
            temp += item[j]
    result.append(temp)
    temp = 0
print(max(result))

