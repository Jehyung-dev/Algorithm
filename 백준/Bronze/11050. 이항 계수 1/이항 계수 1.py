# 이항 계수1 nCk
N, K = list(map(int,input().split()))   #  값을 받음
deno=1  # 팩토리얼 연산을 위해 변수지정
nume=1
for i in range(-K, 0):  # 5C2라면 분자의 5*4를 위해 k번 진행
    deno*=N
    N-=1
for j in range(1,K+1):    # 분모는 k!
    nume*=j

print(deno//nume)