# 조합

import math

n, m = map(int, input().split())
nume = math.factorial(n)
demo = math.factorial(n - m) * math.factorial(m)
print(nume // demo)
