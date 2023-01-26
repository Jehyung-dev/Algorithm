# 평균

import sys

ipt = sys.stdin.readline
N=int(ipt().rstrip())   # 성적 갯수
score_list=list(map(int,ipt().rstrip().split()))    # 점수 리스트
M=max(score_list)   # M은 최고점수
sum=0   # 평균을 구하기위한 합 변수
for j in range(N):
    sum+=(score_list[j]/M*100)  # 점수 조작하여 더하기
print(sum/N)