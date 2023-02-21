# 촌수계산(BFS)

def DFS(num, cnt):
    global ans
    v[num] = 1
    if num == p2:
        ans = cnt
        return
    for i in adj[num]:
        if not v[i]:
            DFS(i, cnt + 1)


n = int(input())
p1, p2 = map(int, input().split())
E = int(input())
adj = [[] for _ in range(n + 1)]
v = [0] * (n + 1)
ans = -1
for _ in range(E):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

DFS(p1, 0)
print(ans)
