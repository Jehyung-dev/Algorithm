# [S/W 문제해결 기본] 3일차 - 회문2

def Binary_search(start, end, arr):
    while start <= end:
        mid = (start + end) // 2
        if Check_palindrome(arr, mid) == None:
            end = mid -1
        else:
            start = mid+1
    return mid

def Check_palindrome(arr, len):
    for i in range(100):
        for j in range(100-len+1):
            for k in range(len//2):
                if arr[i][j+k] != arr[i][j+len-k-1]:
                    break
            else:
                return len

    for i in range(100):
        for j in range(100-len+1):
            for k in range(len//2):
                if arr[j+k][i] != arr[j+len-k-1][i]:
                    break
            else:
                return len
            
for T in range(10):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    for len in range(Binary_search(1, 100, arr)+1, Binary_search(1, 100, arr)-2, -1):
        if Check_palindrome(arr, len) != None:
            print(f'#{T} {len}')
            break
