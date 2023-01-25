# 소수 찾기
def count_prime_num(lst):   # 소수  갯수를 찾는 함수
    prime_num = 0   # 소수의 갯수
    for i in lst:   # 받은 숫자 리스트의 원소를 하나씩 i에 넣음
        cnt = 0 # 1과 자기 자신을 약수로 갖는지 카운트
        for j in range(1, i+1): # 1 ~ 자신의 수까지 나눠지면 cnt +1
            if i%j == 0:
                cnt+=1
        if cnt == 2:    # 나눠지는 카운트가 2개면 소수 +1
            prime_num+=1
    return prime_num    # 소수 갯수를 반환



N = int(input())
lst = list(map(int,input().split()))
print(count_prime_num(lst))