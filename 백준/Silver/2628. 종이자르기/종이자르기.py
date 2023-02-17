# 종이자르기

w, h = map(int, input().split())
r, c = [0, h], [0, w]
max_r, max_c = 0, 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 0:
        r.append(b)
    else:
        c.append(b)
r, c = sorted(r), sorted(c)

for i in range(len(r) - 1):
    if max_r < r[i + 1] - r[i]:
        max_r = r[i + 1] - r[i]
for j in range(len(c) - 1):
    if max_c < c[j + 1] - c[j]:
        max_c = c[j + 1] - c[j]
print(max_r * max_c)
