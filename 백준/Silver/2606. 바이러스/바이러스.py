# 바이러스

def DFS(n):
    global result

    result += 1
    v[n] = 1
    for i in adj[n]:
        if not v[i]:
            DFS(i)


V, E = int(input()), int(input())
adj = [[] for _ in range(V + 1)]
result = 0
v = [0] * (V + 1)
for _ in range(E):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

DFS(1)
print(result-1)
