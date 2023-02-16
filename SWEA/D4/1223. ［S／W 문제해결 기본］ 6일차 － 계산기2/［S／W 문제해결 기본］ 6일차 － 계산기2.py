# [S/W 문제해결 기본] 6일차 - 계산기2

op = {'+': 0, '*': 1}
for t in range(10):
    N = int(input())
    exp = input()
    stack, post = [], ''

    for i in exp:
        if i in op:
            if not stack:
                stack.append(i)
                continue
            else:
                while stack and op[i] <= op[stack[-1]]:
                    post += stack.pop()
                stack.append(i)
        else:
            post += i
    while stack:
        post += stack.pop()

    stack = []
    for j in post:
        if not j in op:
            stack.append(j)
        else:
            b, a = int(stack.pop()), int(stack.pop())
            if j == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)
    print(f'#{t + 1} {stack[0]}')
