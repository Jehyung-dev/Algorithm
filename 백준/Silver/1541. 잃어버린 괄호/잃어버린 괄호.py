# 잃어버린 괄호


def Sum(arr):
    arr = list(map(int, arr.split("+")))
    return sum(arr)


exp = input().split("-")
if "+" in exp[0]:
    ans = Sum(exp[0])
else:
    ans = int(exp[0])
exp.pop(0)

for num in exp:
    if "+" in num:
        ans -= Sum(num)
    else:
        ans -= int(num)

print(ans)
