# 나는야 포켓몬 마스터 이다솜

num, name = {}, {}
N, M = map(int, input().split())

for i in range(1, N+1):
    monster = input()
    num[i] = monster
    name[monster] = i

for _ in range(M):
    ask = input()
    if '0' <= ask[0] <= '9':
        print(num[int(ask)])
    else:
        print(name[ask])
