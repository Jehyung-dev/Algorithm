# [S/W 문제해결 기본] 2일차 - Sum

for _ in range(10):
    t = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]
    row_column_max = 0

    for i in range(100):
        row_sum = 0
        column_sum = 0
        for j in range(100):
            row_sum += num_list[i][j]
            column_sum += num_list[j][i]
            if row_sum > column_sum and row_sum > row_column_max:
                row_column_max = row_sum
            elif column_sum > row_column_max:
                row_column_max = column_sum

    cross_max = 0
    for m in range(100):
        cross_sum1 = 0
        cross_sum2 = 0
        cross_sum1 += num_list[m][m]
        cross_sum2 += num_list[m][99-m]
        if cross_sum1 > cross_sum2 and cross_sum1 > cross_max:
            cross_max = cross_sum1
        elif cross_sum2 > cross_max:
            cross_max = cross_sum2

    if row_column_max > cross_max:
        print(f'#{t} {row_column_max}')
    else:
        print(f'#{t} {cross_max}')
