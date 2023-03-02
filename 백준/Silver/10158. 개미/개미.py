# 개미

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
t_x = t % (2 * w)
t_y = t % (2 * h)
di_x = di_y = 1
cnt = 0

while cnt < t_x:
    nx = x + di_x
    if 0 <= nx <= w:
        x = nx
    else:
        di_x *= -1
        x = x + di_x
    cnt += 1

cnt = 0
while cnt < t_y:
    ny = y + di_y
    if 0 <= ny <= h:
        y = ny
    else:
        di_y *= -1
        y = y + di_y
    cnt += 1

print(x, y)
