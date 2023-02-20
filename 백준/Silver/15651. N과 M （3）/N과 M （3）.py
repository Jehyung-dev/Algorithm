# N과 M (3)

def DFS(n, arr):
    if n == M:
        result.append(arr)
        return

    for i in range(1, N + 1):
        DFS(n + 1, arr + [i])


N, M = map(int, input().split())
result = []

DFS(0, [])
for lst in result:
    print(*lst)
