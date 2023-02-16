# 플로이드

n, m = int(input()), int(input())
INF = int(1e9)
arr = [[INF] * n for _ in range(n)]
for i in range(n):
    arr[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if arr[a - 1][b - 1] > c:
        arr[a - 1][b - 1] = c
for k in range(n):
    for x in range(n):
        for y in range(n):
            if arr[x][y] > arr[x][k] + arr[k][y]:
                arr[x][y] = arr[x][k] + arr[k][y]

for i in arr:
    for j in i:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
