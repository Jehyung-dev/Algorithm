# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())
for _ in range(T):
    case_num = int(input())
    score_list = list(map(int, input().split()))
    count_list = [0]*101
    max_count = 0

    for i in score_list:
        count_list[i] += 1

    for j in range(len(count_list)):
        if max_count <= count_list[j]:
            max_count = count_list[j]
            frequent_number = j

    print(f'#{case_num} {frequent_number}')