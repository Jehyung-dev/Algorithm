# ATM

N = int(input())
P = list(map(int, input().split()))
P = sorted(P, reverse=True)
sum = 0

for i in range(1, N + 1):
    sum += P[i - 1] * i

print(sum)
