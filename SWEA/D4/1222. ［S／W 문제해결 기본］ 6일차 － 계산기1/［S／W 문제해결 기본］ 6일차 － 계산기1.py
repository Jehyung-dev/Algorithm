# [S/W 문제해결 기본] 6일차 - 계산기1

for t in range(10):
    N = int(input())
    exp = input()
    stack, post, top = [], '', -1

    for i in exp:
        if i == '+':
            if stack:
                post += stack.pop()
            stack.append(i)
        else:
            post += i
    if stack:
        post += stack.pop()

    stack = []
    for j in post:
        if j != '+':
            stack.append(j)
        else:
            b, a = int(stack.pop()), int(stack.pop())
            stack.append(a + b)
    print(f'#{t+1} {stack[0]}')
