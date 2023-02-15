# 쇠막대기 자르기

T = int(input())
for t in range(T):
    test = input()
    stick, sum = [], 1
    for i in range(len(test) - 1):
        if test[i] + test[i + 1] == '()':
            sum += len(stick)
        elif test[i] == '(':
            stick.append(1)
        elif stick != [] and test[i - 1] + test[i] != '()' and test[i] == ')':
            sum += 1
            stick.pop()
    print(f'#{t + 1} {sum}')
