# 상수


def Read(n):
    return int(n[2] + n[1] + n[0])


A, B = input().split()

new_A = Read(A)
new_B = Read(B)

if new_A > new_B:
    print(new_A)
else:
    print(new_B)
