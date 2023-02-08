# 가장 빠른 문자열 타이핑

T = int(input())
for t in range(T):
    A, B = input().split()
    count = 0
    i = 0

    while i <= len(A) - len(B):
        str = ''
        for j in range(i, i+len(B)):
            str+=A[j]
        if str != B:
            count += 1
            i += 1
        else:
            count += 1
            i += len(B)

    count += len(A)-i
    print(f'#{t+1} {count}')