# Hashing

import sys
input = sys.stdin.readline
L=int(input().rstrip()) # 문자길이
temp_list=list(input().rstrip())    # 문자열 받음
change_str_num=[]   # 문자를 숫자로 변환
sum=0   #합을 위함
for i in temp_list: # 아스키코드 사용
    change_str_num.append(ord(i)-96)
for j in range(L):
    sum+=change_str_num[j]*(31**j)  # 해시함수 
print(sum%1234567891)