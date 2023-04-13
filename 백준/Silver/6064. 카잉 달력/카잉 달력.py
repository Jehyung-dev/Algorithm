# 카잉 달력

import math


def Cnt(all):
    if M > N:
        i = x
        gap = M
    else:
        i = y
        gap = N
    while i <= all:
        if (i - x) % M == 0 and (i - y) % N == 0:
            return i
        else:
            i += gap
    return -1


for t in range(int(input())):
    M, N, x, y = map(int, input().split())
    all = math.lcm(M, N)

    print(Cnt(all))
