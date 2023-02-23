# 색종이

N = int(input())
square = [[0] * 1001 for _ in range(1001)]

for i in range(1, N + 1):
    c1, r1, w, h = map(int, input().split())
    for r in range(r1, r1 + h):
        for c in range(c1, c1 + w):
            square[r][c] = i

for i in range(1, N + 1):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if square[j][k] == i:
                cnt += 1
    print(cnt)
