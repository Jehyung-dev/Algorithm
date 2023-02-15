# 백만 장자 프로젝트

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt, sum, result = 0, 0, 0

    max = arr[-1]
    for i in range(N - 2, -1, -1):
        if arr[i] > max:
            result += max * cnt - sum
            max = arr[i]
            sum, cnt = 0, 0
        else:
            sum += arr[i]
            cnt += 1
    if cnt != 0:
        result += max * cnt - sum

    print(f'#{t + 1} {result}')
