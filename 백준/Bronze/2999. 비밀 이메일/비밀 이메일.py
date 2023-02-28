# 비밀 이메일

M = input()
L = len(M)
r = c = k = idx = 0
s = ''
for i in range(1, int(L ** (1 / 2)) + 1):
    for j in range(i, L + 1):
        if i * j == L:
            r, c = i, j

for k in range(r):
    for l in range(c):
        s += M[k + l * r]

print(s)
