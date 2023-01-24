# 직각삼각형

while 1:    # 무한 루프
    lst = list(map(int,input().split()))    # 변의 길이를 리스트로 받음
    ord_lst = sorted(lst)   # 길이를 오름차순
    if ord_lst[0] == ord_lst[1] == ord_lst[2] == 0:    # 0 0 0시 종료
        break
    else:   #직각삼각형 right / 아닌 경우 wrong
        if ord_lst[2]**2 == ord_lst[0]**2 + ord_lst[1]**2:
             print('right')
        else:
            print('wrong')