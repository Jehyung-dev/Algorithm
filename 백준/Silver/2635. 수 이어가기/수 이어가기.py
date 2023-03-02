# 수 이어가기

arr = []
N = int(input())
arr = [N]
start = N // 2 + 1
cnt, ans_cnt = 1, 0

for i in range(start, N + 1):
    while i >= 0:
        arr.append(i)
        cnt += 1
        i = arr[-2] - arr[-1]
    if cnt > ans_cnt:
        ans_cnt = cnt
        ans_arr = arr[::]
    cnt = 1
    arr = [N]

print(ans_cnt)
print(*ans_arr)
