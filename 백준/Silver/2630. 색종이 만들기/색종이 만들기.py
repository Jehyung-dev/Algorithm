# 색종이 만들기


def Cnt(r, c, n):
    global W, B

    point = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != point:
                for k in range(2):
                    for l in range(2):
                        Cnt(r + k * n // 2, c + l * n // 2, n // 2)
                return
    color[point] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
color = [0, 0]

Cnt(0, 0, N)

for ans in color:
    print(ans)
