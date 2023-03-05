# 파리 퇴치

def Catch():
    ans = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            temp = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    temp += arr[k][l]
                if temp > ans:
                    ans = temp
    return ans


for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t + 1} {Catch()}')
