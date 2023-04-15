# # 경로 찾기

from collections import deque


def BFS(k):
    global point, G

    Q = deque([k])
    check = [0] * N

    while Q:
        s = Q.popleft()
        check[s] = 1
        for m in arr[s]:
            if m == point:
                return 1
            elif not check[m]:
                Q.append(m)
    return 0


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
arr = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if G[i][j]:
            arr[i].append(j)

for k in range(N):
    for l in range(N):
        if not G[k][l]:
            point = l
            if BFS(k):
                G[k][l] = 1

for g in G:
    print(*g)
