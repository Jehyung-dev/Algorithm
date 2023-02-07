# 숫자를 정렬하자

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(f'#{t+1} ', end='')
    print(*arr)