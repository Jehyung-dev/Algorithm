# 팩토리얼 0의 개수

fac, ans = 1, 0
for i in range(1, int(input())+1):
    fac *= i

while 1:
    if fac % 10 == 0:
        fac //= 10
        ans += 1
    else:
        break

print(ans)
