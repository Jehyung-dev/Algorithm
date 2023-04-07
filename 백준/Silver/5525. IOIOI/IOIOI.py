# IOIO

N, M = int(input()), int(input())
S = input()
cnt = ans = i = 0

while i <= M - 3:
    if S[i] == "I" and S[i + 1] == "O" and S[i + 2] == "I":
        cnt += 1
        i += 2
    else:
        if cnt >= N:
            ans += cnt - N + 1
        cnt = 0
        i += 1

if cnt >= N:
    ans += cnt - N + 1

print(ans)
