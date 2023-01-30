# 나무 자르기

import sys
input = sys.stdin.readline
output = sys.stdout.write
N, M = map(int,input().rstrip().split())
tree_height_list = list(map(int,input().rstrip().split()))
min_num = 1
max_num = max(tree_height_list)
result=0

while min_num<=max_num:
    mid = (min_num+max_num)//2
    tree_get = 0

    for i in tree_height_list:
        if i>=mid:
            tree_get+=(i-mid)
    
    if tree_get < M:
        max_num = mid-1
    else:
        min_num=mid+1
        result=mid
print(result)