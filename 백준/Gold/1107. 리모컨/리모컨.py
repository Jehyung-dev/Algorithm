# 리모컨

N = int(input())
M = int(input())
broken = set()
if M:
    broken = set(input().split())

cnt1 = abs(N - 100)
cnt2 = int(1e9)

for num in range(1000001):
    num = str(num)
    if not set(num) & broken:
        tmp = abs(int(num) - N) + len(num)
        if tmp < cnt2:
            cnt2 = tmp

print(min(cnt1, cnt2))
