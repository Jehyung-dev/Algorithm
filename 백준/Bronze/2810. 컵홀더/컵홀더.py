# 컵홀더

N = int(input())
seat = input()
i = cnt = 0

while i < N:
    if seat[i] == 'S':
        i += 1
        cnt += 1
    else:
        i += 2
        cnt += 1

if cnt + 1 > N:
    print(N)
else:
    print(cnt + 1)
