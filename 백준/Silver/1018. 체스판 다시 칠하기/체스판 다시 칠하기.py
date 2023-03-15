# 체스판 다시 칠하기

def W(r, c):
    cnt = 0
    for i in range(r, r+8):
        for j in range(c, c+8):
            if (i+j) % 2 == 0 and arr[i][j] != 'W':
                cnt += 1
            elif (i+j) % 2 == 1 and arr[i][j] != 'B':
                cnt += 1
    return cnt


def B(r, c):
    cnt = 0
    for i in range(r, r+8):
        for j in range(c, c+8):
            if (i+j) % 2 == 0 and arr[i][j] != 'B':
                cnt += 1
            elif (i+j) % 2 == 1 and arr[i][j] != 'W':
                cnt += 1
    return cnt


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
Min = 2500

for r in range(0, N-7):
    for c in range(0, M-7):
        temp = min(W(r, c), B(r, c))
        if temp < Min:
            Min = temp

print(Min)
