# ACM 호텔

T = int(input())
for _ in range(T):
    H,W,N = list(map(int,input().split()))    # H :층 갯수 / W : 방 갯수, N : 도착 순서
    if  N%H != 0:   # 나눠떨어지면 0이 아니라 제일 위층
        print(f'{N%H}{N//H+1:0>2}') # {숫자 : 0>2}는 2자리로 늘려 부족한 것을 0으로 채움
    else:
        print(f'{H}{N//H:0>2}')