# N과 M (1)

def DFS(n, arr):
    if n == M:
        result.append(arr)
        return

    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            DFS(n + 1, arr + [i])
            visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N + 1)
result = []
DFS(0, [])

for lst in result:
    print(*lst)
