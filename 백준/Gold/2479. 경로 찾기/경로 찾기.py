# 경로 찾기

def Graph():
    for x in range(N - 1):
        for y in range(x + 1, N):
            cnt = 0
            for z in range(K):
                if arr[x][z] != arr[y][z]:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                H[x + 1].append(y + 1)
                H[y + 1].append(x + 1)


def DFS(start, dist):
    global Min, temp, ans
    visited[start] = 1

    if Min > dist:
        Min = dist

    if start == B:
        ans += temp

    for i in H[start]:
        if not visited[i]:
            temp.append(i)
            DFS(i, dist + 1)
            dist -= 1
            temp.pop()


N, K = map(int, input().split())
arr = [input() for _ in range(N)]
H = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
A, B = map(int, input().split())
Min, temp, ans = 100, [], [A]

Graph()
DFS(A, 0)

if len(ans) == 1:
    print(-1)
else:
    print(*ans)
