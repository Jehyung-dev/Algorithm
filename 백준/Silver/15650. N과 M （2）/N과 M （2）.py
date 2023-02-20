# N과 M (2)

def DFS(n, arr):
    if n == M:
        arr = sorted(arr)
        if not arr in result:
            result.append(arr)
        return
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            DFS(n + 1, arr + [i])
            visited[i] = 0


N, M = map(int, input().split())
result = []
visited = [0] * (N + 1)
DFS(0, [])

for lst in result:
    print(*lst)
