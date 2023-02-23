# 직사각형 네개의 합집합의 면적 구하기

arr = [list(map(int, input().split())) for _ in range(4)]
range_r, range_c, cnt = 0, 0, 0
for c1, r1, c2, r2 in arr:
    if c2 > range_c:
        range_c = c2
    if r2 > range_r:
        range_r = r2

square = [[0] * range_c for _ in range(range_r)]
for c1, r1, c2, r2 in arr:
    for r in range(range_r - r2, range_r - r1):
        for c in range(c1, c2):
            square[r][c] = 1

for i in square:
    for j in i:
        if j == 1:
            cnt += 1
print(cnt)
