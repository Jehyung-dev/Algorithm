# 비밀번호 찾기

dic = {}
N, M = map(int, input().split())
for _ in range(N):
    site, pwd = input().split()
    dic[site] = pwd

for _ in range(M):
    print(dic[input()])
