# 수열

N = int(input())
arr = list(map(int, input().split()))
inc_cnt = [1] * N
dec_cnt = [1] * N

for i in range(N - 1):
    if arr[i] <= arr[i + 1]:
        inc_cnt[i + 1] = inc_cnt[i] + 1
    if arr[i] >= arr[i + 1]:
        dec_cnt[i + 1] = dec_cnt[i] + 1

print(max(max(inc_cnt), max(dec_cnt)))
