# 팰린드롬수

while 1:    # 무한 루프
    n = input() # 리스트 변환을 위해 문자열로 받음
    if n =='0': # 0입력시 종료
        break
    n = list(n)
    if n == n[::-1]:    # 리스트와 역순의 리스트가 같을 경우 yes출력
        print('yes')
    else:   # 아닐경우 no출력
        print('no')