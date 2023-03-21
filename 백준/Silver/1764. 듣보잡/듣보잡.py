# 듣보잡

dic = {}
ans = []
cnt = 0
N, M = map(int, input().split())
for _ in range(N):
    dic[input()] = 1

for _ in range(M):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

for i in dic:
    if dic[i] == 2:
        ans.append(i)
        cnt += 1

ans.sort()
print(cnt)
for j in ans:
    print(j)
