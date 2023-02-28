# 영식이와 친구들

N, M, L = map(int, input().split())
num = [0] * (N + 1)
ball, cnt = 1, 0

while not M in num:
    num[ball] += 1
    if num[ball] % 2:
        ball = (ball + L % N) % N
    else:
        ball = (N + ball - L % N) % N
    cnt += 1

print(cnt - 1)
