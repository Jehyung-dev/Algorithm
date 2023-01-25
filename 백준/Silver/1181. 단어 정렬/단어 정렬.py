# 단어 정렬

N = int(input())    # 단어 갯수 입력
lst = []    # 단어들을 넣을 리스트
for i in range(N):
    lst.append(input())
lst = set(lst)  # 중복 제거를 위해 set자료형 사용
chng_lst = sorted(lst, key=lambda x : (len(x), x))  # 우선조건을 생각하여 정렬, 자료형은 리스트로 자동변환
for j in chng_lst:  # 출력
    print(j)