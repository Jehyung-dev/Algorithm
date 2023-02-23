# 색종이

square = [[0] * 101 for _ in range(101)]
cnt = 0
T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    for r in range(h, h + 10):
        for c in range(w, w + 10):
            square[r][c] = 1

for i in range(101):
    for j in range(101):
        if square[i][j]:
            cnt += 1
print(cnt)
