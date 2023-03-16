# 스택 수열

def Put():
    global ans, stack
    idx_arr, idx_ord = 0, 0
    while 1:
        if arr[idx_arr] in stack and arr[idx_arr] != stack[-1]:
            return 0
        elif arr[idx_arr] in stack:
            ans.append('-')
            stack.pop()
            idx_arr += 1
        elif arr[idx_arr] >= ord[idx_ord]:
            ans.append('+')
            stack.append(ord[idx_ord])
            idx_ord += 1
        if idx_arr == n:
            return 1


n = int(input())
ord, arr, ans, stack = [], [], [], []
idx = 0

for _ in range(n):
    arr.append(int(input()))

for i in range(1, n+1):
    ord.append(i)

if Put():
    for j in ans:
        print(j)
else:
    print('NO')
