# 최대공약수와 최소공배수

n1, n2 = list(map(int,input().split())) # 두 수를 받음
GCM = 0 # 최대공약수
if n1>= n2:  # 1부터 작은수까지
    for i in range(1,n2+1):
        if n1%i == 0 and n2%i == 0: # 모두 나눠떨어지는 최대수를 대입
            GCM = i
else:
    for i in range(1,n1+1):
        if n1%i == 0 and n2%i == 0:
            GCM = i
print(GCM)
print((n1//GCM)*(n2//GCM)*GCM)  # 각 수를 최대공약수로 나누고 최대공약수*나머지1*나머지2하면 최소공배수가 나옴