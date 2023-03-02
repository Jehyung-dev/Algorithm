# 색종이 - 2

def Check(r, c):
    global cnt
    for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        if 0 <= nr < 101 and 0 <= nc < 101 and not arr[nr][nc]:
            cnt += 1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N = int(input())
arr = [[0] * 101 for _ in range(101)]
cnt = 0

for _ in range(N):
    c, r = map(int, input().split())
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            arr[i][j] = 1

for x in range(101):
    for y in range(101):
        if arr[x][y]:
            Check(x, y)

print(cnt)
