# 최단경로

import heapq

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(K):
    q = []
    dist[K] = 0
    heapq.heappush(q, (0, K))
    while q:
        now_dist, now = heapq.heappop(q)
        if dist[now] < now_dist:
            continue
        for i in graph[now]:
            cost = now_dist + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])