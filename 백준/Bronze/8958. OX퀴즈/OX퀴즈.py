# OX퀴즈

T = int(input())

for _ in range(T):
    Quiz = input()
    cnt = sum = 0

    for i in range(len(Quiz)):
        if Quiz[i] == 'O':
            cnt += 1
            sum += cnt
        if Quiz[i] == 'X':
            cnt = 0

    print(sum)
