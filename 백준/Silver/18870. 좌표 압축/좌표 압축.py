# 좌표 압축

N = int(input())
arr = list(map(int, input().split()))
new_arr = set(arr)
new_arr = sorted(new_arr, key=lambda x: x)
dic = {}

for i in range(len(new_arr)):
    dic[new_arr[i]] = i

for j in arr:
    print(dic[j], end=" ")
