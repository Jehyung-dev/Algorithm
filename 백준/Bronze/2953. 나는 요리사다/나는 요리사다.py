# 나는 요리사다

import sys
input = sys.stdin.readline
score_list = [] # 점수 리스트
for i in range(5):  # 5명의 참가자라 5번 반복
    score_list.append((i+1,sum(list(map(int,input().rstrip().split()))))) # 번호, 점수 합을 튜플 형태로 리스트에 추가
score_list.sort(key = lambda x: x[1], reverse=True) # 점수를 기준으로 내림차순
print(score_list[0][0], score_list[0][1])   # 번호와 점수를 출력