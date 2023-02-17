# 더하기 사이클

N = input()
if len(N) == 1:
    N = '0' + N
new_N = N
cnt = 0

while 1:
    temp = (int(new_N[0]) + int(new_N[1])) % 10
    new_N = new_N[1] + str(temp)
    cnt += 1
    if N == new_N:
        break
print(cnt)
