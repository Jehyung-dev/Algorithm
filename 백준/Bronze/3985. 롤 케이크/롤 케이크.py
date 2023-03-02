# 롤 케이크

L, N = int(input()), int(input())
arr = [0] * (L + 1)
audience = []
Max = real_Max = idx = real_idx = 0

for i in range(1, N + 1):
    a, b = map(int, input().split())
    audience.append((a, b))
    if b - a+1 > Max:
        Max = b - a+1
        idx = i

for j in audience:
    c, d = j
    for k in range(c, d + 1):
        arr[k] += 1
    temp = arr[c:d+1].count(1)
    if temp > real_Max:
        real_Max = temp
        real_idx = audience.index(j) + 1

print(idx)
print(real_idx)
