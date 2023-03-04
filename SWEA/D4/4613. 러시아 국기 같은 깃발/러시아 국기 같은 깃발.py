# 러시아 국기 같은 깃발

def Cnt(start, end, color):
    temp = 0
    for i in range(start, end + 1):
        temp += M - arr[i].count(color)
    return temp


for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = set()

    for end1 in range(0, N - 2):
        for end2 in range(end1 + 1, N - 1):
            ans.add(Cnt(0, end1, 'W') + Cnt(end1 + 1, end2, 'B') + Cnt(end2 + 1, N - 1, 'R'))

    print(f'#{t + 1} {min(ans)}')
