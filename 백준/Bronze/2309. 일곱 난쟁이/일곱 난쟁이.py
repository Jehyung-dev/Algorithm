# 일곱 난쟁이

def DFS(n, sum):
    global result
    if 100 < sum:
        return

    if n == 7 and sum == 100:
        result = visited[::]
        return
    for i in range(9):
        if visited[i] == 0:
            visited[i] = 1
            DFS(n + 1, sum + arr[i])
            visited[i] = 0


arr = [int(input()) for _ in range(9)]
visited, result,new= [0] * 9, []*9, []
DFS(0, 0)
for i in range(9):
    if result[i] == 1:
        new.append(arr[i])
new = sorted(new)
for j in new:
    print(j)