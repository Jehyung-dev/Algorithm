# 연속한 1의 개수

T = int(input())    # 반복 횟수
for t in range(T):  
    N = int(input())    # 0과 1의 갯수
    string = input()   # 문자열로 받음

    for i in range(N, -1, -1):  # i는 N개부터 0까지 역순
        if '1'*i in string: # 최대한 많은 1의 문자열을 만나면 중지
            break
    print(f'#{t+1} {i}')    # 그 횟수를 출력