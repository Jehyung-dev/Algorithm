# [S/W 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())    # 총 테스트 케이스를 받음
for _ in range(T):
    case_num = int(input()) # 테스트 케이스의 번호
    score_list = list(map(int, input().split()))    # 점수를 리스트로 변환
    count_list = [0]*101    # 0이상 100이하이므로 초기값 0 으로 101개의 항을 만듦
    max_count = 0   # 최빈값의 횟수를 저장할 변수

    for i in score_list:    # 모든 점수를 인덱스로 카운트를 +1씩 반복함
        count_list[i] += 1

    for j in range(len(count_list)):    # 카운트 리스트의 길이만큼 반복하며
        if max_count <= count_list[j]:  # 최빈값의 갯수가 더 많은 것이 나오면
            max_count = count_list[j]   # 최빈값의 갯수를 교체
            frequent_number = j         # 그 순간의 숫자(최빈값을 저장)

    print(f'#{case_num} {frequent_number}') # 출력
