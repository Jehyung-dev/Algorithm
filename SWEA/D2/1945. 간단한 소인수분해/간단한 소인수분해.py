# 간단한 소인수분해

def devision(num, index):   # 나눠주는 함수
    count = 0   # 리턴값
    while 1:    # 무한 루프
        if num%index == 0:  # 몇 번 나눌 수 있는지
            count += 1
            num = num//index
        else:   # 나눌 수 없다면 중지
            break
    return count

T = int(input())    # 반복 횟수
for t in range(T):
    num = int(input())  # 받은 숫자
    num_list = [2, 3, 5, 7, 11] # 나눌 숫자
    lst = [0]*12    # 카운트 솔팅

    for i in num_list:
        lst[i] = devision(num, i)
    print(f'#{t+1} {lst[2]} {lst[3]} {lst[5]} {lst[7]} {lst[11]}')