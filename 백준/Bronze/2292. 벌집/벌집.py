# 벌집

N = int(input())
cnt = 1

if N == 1:
    print(1)
else:
    start, end = 2, 7
    while N < start or end < N:
        start += 6 * cnt
        end += 6 * (cnt + 1)
        cnt += 1

    print(cnt + 1)
