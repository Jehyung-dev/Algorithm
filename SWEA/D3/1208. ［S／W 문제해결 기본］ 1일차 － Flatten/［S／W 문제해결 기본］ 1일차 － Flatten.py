# [S/W 문제해결 기본] 1일차 - Flatten

for t in range(10): # 10번 반복
    dump = int(input()) # dump 횟수 받기
    num_list = list(map(int, input().split()))  # 숫자 리스트 입력
    dump_count = 0  # 덤프 반복 횟수 카운트

    while dump_count != dump:   # 최대, 최소 인덱스를 이용하여 찾아 각각 -1, +1진행
        max_index = 0
        min_index = 0
        for i in range(1, len(num_list)):
            if num_list[max_index] < num_list[i]:
                max_index = i
        for j in range(1, len(num_list)):
            if num_list[min_index] > num_list[j]:
                min_index = j
        num_list[max_index] -= 1
        num_list[min_index] += 1
        dump_count += 1

    max_index = 0   # 마지막 반복 후 최대, 최소가 변경될 수 있기에 새로 찾음
    min_index = 0
    for i in range(1, len(num_list)):
        if num_list[max_index] < num_list[i]:
            max_index = i
    for j in range(1, len(num_list)):
        if num_list[min_index] > num_list[j]:
            min_index = j
    print(f'#{t+1} {num_list[max_index]-num_list[min_index]}')