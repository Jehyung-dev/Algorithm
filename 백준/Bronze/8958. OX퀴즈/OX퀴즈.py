# OX퀴즈

cnt = 0
sum = 0
n = int(input())

for i in range(n):
    Quiz = list(input())

    for j in range(len(Quiz)):
        if Quiz[j] == 'O':
            cnt += 1
            sum += cnt
        if Quiz[j] == 'X':
            cnt = 0
    print(sum)
    sum = 0
    cnt = 0