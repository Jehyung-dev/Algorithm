# 아스키 코드

import sys

ipt = sys.stdin.readline
char = ipt().rstrip()   # 하나의 글자를 받음
print(ord(char))    # 아스키 코드 출력