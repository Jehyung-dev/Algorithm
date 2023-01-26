# N 찍기

import sys
ipt = sys.stdin.readline
print_set=set(i for i in range(1, int(ipt().rstrip())+1))   # 1부터 입력값까지의 set를 만듦
s=''
for i in print_set: # 하나씩 출력하는 형태를 문자열로 만들어 출력
    s+=str(i)+'\n'
print(s)