# 세제곱근을 찾아라

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = int(N**(1/3))
    for i in range(num, num+2):
        if i*i*i == N:
            print(f'#{t} {i}')
            break
    else:
        print(f'#{t} -1')
