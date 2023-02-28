# 직사각형을 만드는 방법

n = int(input())
i = j = 1
cnt = 0

while i * i <= n:
    if i * j <= n:
        j += 1
        cnt += 1
    else:
        i += 1
        j = i

print(cnt)
