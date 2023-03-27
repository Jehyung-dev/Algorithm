# 마인크래프트


def Build(i, b):
    global ans, high
    time = 0
    for j in arr:
        if i > j:
            time += i - j
            b -= i - j

        elif i < j:
            time += (j - i) * 2
            b += j - i

    if b >= 0 and time < ans:
        ans = time
        high = i
    elif b >= 0 and time == ans and high < i:
        high = i


N, M, B = map(int, input().split())
arr = []
ans, high = int(1e9), 0

for _ in range(N):
    arr += list(map(int, input().split()))

for i in range(min(arr), max(arr) + 1):
    Build(i, B)

print(f"{ans} {high}")
