# 최대 힙

import sys, heapq

input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, (-x, x))
    elif heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)
