# 스도쿠 검증

def Check_line():
    for i in range(9):
        temp = set()
        if len(set(arr[i])) != 9:
            return 0
        for j in range(9):
            temp.add(arr[j][i])
        if len(temp) != 9:
            return 0
    return 1


def Check_box():
    for i in range(3):
        for j in range(3):
            temp = set()
            for k in range(3 * i, 3 * (i + 1)):
                for l in range(3 * j, 3 * (j + 1)):
                    temp.add(arr[k][l])
            if len(temp) != 9:
                return 0
    return 1


for t in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if Check_line() and Check_box():
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')
