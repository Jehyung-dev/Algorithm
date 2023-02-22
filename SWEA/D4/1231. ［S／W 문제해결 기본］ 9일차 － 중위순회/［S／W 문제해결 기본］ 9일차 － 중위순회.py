# [S/W 문제해결 기본] 9일차 - 중위순회

def inord(n):
    if n <= N:
        inord(n*2)
        ans.append(g[n])
        inord(n*2+1)

for t in range(1,11):
    N = int(input())
    g = [0]*(N+1)
    for _ in range(N):
        arr = input().split()
        idx = arr[0]
        g[int(idx)] = arr[1]

    ans = []
    inord(1)

    print(f'#{t} {"".join(ans)}')