# [S/W 문제해결 기본] 3일차 - 회문1

def check_palindrome(arr, len):
    count = 0
    for i in range(8):
        for j in range(8-len+1):
            for k in range(len//2):
                if arr[i][j+k] != arr[i][j+len-k-1]:
                    break
            else:
                count += 1
    for i in range(8):
        for j in range(8-len+1):
            for k in range(len//2):
                if arr[j+k][i] != arr[j+len-k-1][i]:
                    break
            else:
                count += 1
    return count



for T in range(10):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    print(f'#{T+1} {check_palindrome(arr, length)}')
