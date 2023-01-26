# 최소, 최대

import sys

ipt = sys.stdin.readline
T=int(ipt().rstrip())
number_list=list(map(int,ipt().rstrip().split()))
print(min(number_list),max(number_list))