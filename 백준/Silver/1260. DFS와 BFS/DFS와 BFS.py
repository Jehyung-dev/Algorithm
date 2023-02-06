# DFS와 BFS
from collections import deque

N, M, V = map(int, input().split())
visited = [False] * (N + 1)
arr = [[] for _ in range(N + 1)]
graph = [[]]
for _ in range(M):
    num1, num2 = list(map(int, input().split()))
    arr[num1].append(num2)
    arr[num2].append(num1)
for i in range(1, N + 1):
    graph.append(sorted(arr[i]))


def dfs(graph, visited, V):
    visited[V] = True
    print(f'{V}', end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, V):
    visited[V] = True
    queue = deque([V])
    while queue:
        V = queue.popleft()
        print(f'{V}', end=' ')
        for i in graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, visited, V)
print()
visited = [False] * (N+1)
bfs(graph, visited, V)
