# 통계학

def Freq():
    ans = cnt = 0
    Max = max(dic.values())
    for j in dic:
        if dic[j] == Max:
            cnt += 1
            ans = j
        if cnt == 2:
            return ans
    return ans


N = int(input())
dic = {}
arr = [int(input()) for _ in range(N)]
arr.sort()

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(int(round(sum(arr)/N, 0)))
print(arr[N//2])
print(Freq())
print(arr[N-1]-arr[0])
