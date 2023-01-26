S = str(input())
S = S.upper()
S_list = list(set(S))

cnt = []
for i in range(len(S_list)):
    cnt.append(list(S).count(S_list[i]))
Max = max(cnt)
if cnt.count(Max) != 1:
    print("?")
else:
    print(S_list[cnt.index(Max)])