# 줄 세우기

N = int(input())
arr = list(map(int, input().split()))
line = []

for i in range(N):
    line.insert(i - arr[i], i + 1)
    
print(*line)
