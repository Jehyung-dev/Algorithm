# N과 M (1)  /   순열문제(재귀)

N, M = map(int, input().split())    # N과 M입력 
lst = []    # 리스트 선언

def back():
    if len(lst) == M:   # 리스트 길이가 받는 수까지
        print(*lst) # 리스트 그냥 출력
        return  # back()이후로 리턴
    for i in range(1, N+1):
        if i not in lst:    # 없다면 아래 실행
            lst.append(i)
            back()
            lst.pop()

back()

