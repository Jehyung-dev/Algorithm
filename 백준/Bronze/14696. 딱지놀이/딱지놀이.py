# 딱지놀이

N = int(input())
for _ in range(N):
    size, *type = list(map(int, input().split()))
    a = [0] * (5)
    for i in type:
        a[i] += 1

    size, *type = list(map(int, input().split()))
    b = [0] * (5)
    for j in type:
        b[j] += 1

    for k in range(4, 0, -1):
        if a[k] > b[k]:
            print('A')
            break
        elif a[k] < b[k]:
            print('B')
            break
        else:
            continue
    else:
        print('D')
