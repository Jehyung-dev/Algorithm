# 방 배정

N, K = map(int, input().split())
M, W = [0] * 7, [0] * 7
room = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if S:
        M[Y] += 1
    else:
        W[Y] += 1

for i in range(1, 7):
    if M[i] % K:
        Mroom = M[i] // K + 1
    else:
        Mroom = M[i] // K
    room += Mroom

for j in range(1, 7):
    if W[j] % K:
        Wroom = W[j] // K + 1
    else:
        Wroom = W[j] // K
    room += Wroom

print(room)
