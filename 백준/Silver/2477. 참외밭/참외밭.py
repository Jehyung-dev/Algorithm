# 참외밭

K = int(input())
arr, r, c, max_r, max_c = [], [], [], 0, 0
blank = 1
for i in range(6):
    di, length = map(int, input().split())
    arr.append(length)
    if di < 3:
        c.append(length)
        if max_c < length:
            max_c = length
    else:
        r.append(length)
        if max_r < length:
            max_r = length

if max_r == max_c:
    for i in range(6):
        if arr[i] == max_r:
            r_Idx = i
    for j in range(5, -1, -1):
        if arr[j] == max_c:
            c_Idx = j
else:
    r_Idx = arr.index(max_r)
    c_Idx = arr.index(max_c)
arr[r_Idx] = 0
arr[c_Idx] = 0

if r_Idx != 0:
    arr[r_Idx - 1] = 0
else:
    arr[-1] = 0
if c_Idx != 0:
    arr[c_Idx - 1] = 0
else:
    arr[-1] = 0
if r_Idx != 5:
    arr[r_Idx + 1] = 0
else:
    arr[0] = 0
if c_Idx != 5:
    arr[c_Idx + 1] = 0
else:
    arr[0] = 0

for num in arr:
    if num != 0:
        blank *= num
print((sum(r) // 2 * sum(c) // 2 - blank) * K)
