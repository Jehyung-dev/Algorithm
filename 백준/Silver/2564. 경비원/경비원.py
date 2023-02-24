# 경비원

arr = long = []
w, h = map(int, input().split())
store = int(input())
ans = 0

for _ in range(store + 1):
    a, b = map(int, input().split())
    if a == 1:
        arr.append((0, b))
    elif a == 2:
        arr.append((h, b))
    elif a == 3:
        arr.append((b, 0))
    else:
        arr.append((b, w))

sr, sc = arr.pop()
if a % 2:
    opp = a + 1
else:
    opp = a - 1

while arr:
    r, c = arr.pop()
    if opp == 1 and r == 0:
        ans += h + min(sc + c, w * 2 - sc - c)
    elif opp == 2 and r == h:
        ans += h + min(sc + c, w * 2 - sc - c)
    elif opp == 3 and c == 0:
        ans += w + min(sr + r, h * 2 - sr - r)
    elif opp == 4 and c == w:
        ans += w + min(sr + r, h * 2 - sr - r)
    else:
        ans += abs(sr - r) + abs(sc - c)
print(ans)
