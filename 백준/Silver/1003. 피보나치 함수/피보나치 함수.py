# 피보나치 함수


def fib(n):
    if n in dic:
        return dic[n]
    dic[n] = (fib(n - 2)[0] + fib(n - 1)[0], fib(n - 2)[1] + fib(n - 1)[1])
    return dic[n]


dic = {0: ((1, 0)), 1: ((0, 1))}
for t in range(int(input())):
    N = int(input())
    print(*fib(N))
