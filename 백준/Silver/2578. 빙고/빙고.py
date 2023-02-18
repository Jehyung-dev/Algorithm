# 빙고
def Del(num):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 0
                return i, j


def Bingo(r, c):
    global cnt
    for i in range(5):
        if arr[r][i] != 0:
            break
    else:
        cnt += 1

    for j in range(5):
        if arr[j][c] != 0:
            break
    else:
        cnt += 1

    if r == c:
        for k in range(5):
            if arr[k][k] != 0:
                break
        else:
            cnt += 1

    if c == 4 - r:
        for l in range(5):
            if arr[l][4 - l] != 0:
                break
        else:
            cnt += 1


arr = [list(map(int, input().split())) for _ in range(5)]
call = []
cnt = 0
for _ in range(5):
    call += list(map(int, input().split()))

for i in call:
    r, c = Del(i)
    Bingo(r, c)
    if cnt >= 3:
        print(call.index(i) + 1)
        break
