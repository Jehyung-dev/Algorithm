# 크로스워드 만들기

import sys
input = sys.stdin.readline
A, B = input().rstrip().split() # A와 B 문자열 세팅
square_frame = [['.']*len(A) for i in range(len(B))]    # 미리 .을 세팅
for cross_word in A: # 겹치는 단어
    if cross_word in B:
        break

for i in range(len(A)): # 겹치는 부분을 위주로 A, B 세팅
    square_frame[B.index(cross_word)][i]=A[i]
for j in range(len(B)):
    square_frame[j][A.index(cross_word)] = B[j]
for k in square_frame:  # 출력
    print(''.join(k))