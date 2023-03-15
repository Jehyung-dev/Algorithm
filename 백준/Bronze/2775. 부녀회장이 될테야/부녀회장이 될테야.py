# 부녀회장이 될테야

def People(k, n):
    if k == 0:
        arr[k][n] = n
        return n
    if n == 1:
        arr[k][n] = 1
        return 1
    if arr[k][n] != 0:
        return arr[k][n]
    arr[k][n] = People(k-1, n) + People(k, n-1)
    return arr[k][n]


T = int(input())
for _ in range(T):
    k, n = int(input()), int(input())
    arr = [[0]*(n+1) for _ in range(k+1)]
    ans = People(k, n)
    print(ans)
