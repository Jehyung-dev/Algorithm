# 숫자를 정렬하자

T = int(input())    # 반복 횟수
for t in range(T):
    n = int(input())  # 주어진 숫자
    num_list = list(map(int, input().split()))  # 숫자 리스트
    for i in range(n, 0, -1):   # 버블솔팅
        for j in range(i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    print(f'#{t+1}', end=' ')   # 문제 요구대로 출력
    print(*num_list)