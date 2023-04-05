# Z

N, sr, sc = map(int, input().split())
cnt = 0

while N > 1:
    n = 2**N // 2

    if sr < n and sc >= n:
        cnt += n**2
        sc -= n
    elif sr >= n and sc < n:
        cnt += n**2 * 2
        sr -= n
    elif sr >= n and sc >= n:
        cnt += n**2 * 3
        sr -= n
        sc -= n

    N -= 1

print(cnt + sr * 2 + sc)
