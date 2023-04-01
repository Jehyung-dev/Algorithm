# 종이의 개수


def Cnt(r, c, n):
    point = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != point:
                for k in range(3):
                    for l in range(3):
                        Cnt(r + k * n // 3, c + l * n // 3, n // 3)
                return

    ans[point + 1] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [0] * 3

Cnt(0, 0, N)

for m in ans:
    print(m)
