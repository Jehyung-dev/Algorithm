# 쉽게 푸는 문제

A, B = map(int, input().split())
lst = []
i = 1
start_sum = 0
end_sum = 0

while len(lst) <= B:
    lst += [i] * i
    i += 1
for i in range(A-1):
    start_sum += lst[i]
for i in range(B):
    end_sum += lst[i]
print(end_sum - start_sum)
