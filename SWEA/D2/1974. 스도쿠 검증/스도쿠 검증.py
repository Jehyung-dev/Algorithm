# 스도쿠 검증

T = int(input())

for i in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    chk_lst1 = [[] for _ in range(9)]
    chk_lst2 = [[] for _ in range(9)]
    chk_lst3 = [[] for _ in range(9)]
    err = 0

    for j in range(9):
        for k in range(9):
            chk_lst1[j].append(arr[k][j])
            chk_lst2[j].append(arr[j][k])

    for m in range(0, 3):
        for n in range(0, 3):
            for o in range(0, 3):
                chk_lst3[m].append(arr[o + m * 3][n])
    for m in range(3, 6):
        for n in range(0, 3):
            for o in range(0, 3):
                chk_lst3[m].append(arr[o][n + 3])
    for m in range(6, 9):
        for n in range(0, 3):
            for o in range(0, 3):
                chk_lst3[m].append(arr[o][n + 6])

    for l in range(9):
        if len(chk_lst1[l]) != len(set(chk_lst1[l])) or len(chk_lst2[l]) != len(set(chk_lst2[l])) or len(
                chk_lst3[l]) != len(set(chk_lst3[l])):
            err += 1
            break

    if err == 0:
        print(f'#{i + 1} 1')
    else:
        print(f'#{i + 1} 0')