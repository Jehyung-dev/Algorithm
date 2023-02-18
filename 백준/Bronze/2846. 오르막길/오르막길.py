# 오르막길

def Uphill(start):
    for i in range(start, N):
        if arr[i] >= arr[i+1]:
           return arr[i] - arr[start], i+1


N = int(input())
arr = list(map(int, input().split())) + [0]
start, gap = 0, set()

while start != N:
    result, start = Uphill(start)
    gap.add(result)
print(max(gap))