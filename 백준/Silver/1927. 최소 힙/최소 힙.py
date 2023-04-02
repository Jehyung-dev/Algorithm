# 최소 힙

import heapq, sys

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)
