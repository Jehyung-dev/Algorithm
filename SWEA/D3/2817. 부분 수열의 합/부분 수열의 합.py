# 부분 수열의 합

def DFS(n, sum):
    global result
    if sum > K:
        return
    if n == N:
        if sum == K:
            result += 1
        return
    DFS(n + 1, sum + arr[n])
    DFS(n + 1, sum)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    DFS(0, 0)
    print(f'#{t + 1} {result}')
