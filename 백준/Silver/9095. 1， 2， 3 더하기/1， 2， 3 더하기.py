# 1, 2, 3 더하기


def Cnt(three, two, one):
    total = three + two + one
    return Fac(total) // Fac(three) // Fac(two) // Fac(one)


def Fac(num):
    result = 1
    if num > 1:
        for x in range(num, 1, -1):
            result *= x

    return result


for _ in range(int(input())):
    n = int(input())
    ans = 0

    for i in range(n // 3 + 1):
        for j in range(n // 2 + 1):
            k = n - (i * 3)
            k -= j * 2
            if k < 0:
                continue
            ans += Cnt(i, j, k)

    print(ans)
