# 2×n 타일링

T = int(input())
dp = [0]*1100   # n 최대값에 + 100 더 할당
dp[1] = 1   #    초기값 설정
dp[2] = 2

for i in range(3, T+1): # 3부터 T까지 계산
    dp[i] = (dp[i-2] + dp[i-1])%10007   # 계산 중에 바로 나누기
print(dp[T])