# 절대값 힙

import heapq
import sys

input = sys.stdin.readline
N = int(input())
m_heap, p_heap = [], []

for _ in range(N):
    x = int(input())

    if x < 0:
        heapq.heappush(m_heap, -x)
    elif x > 0:
        heapq.heappush(p_heap, x)
    elif m_heap and p_heap:
        if m_heap[0] <= p_heap[0]:
            print(heapq.heappop(m_heap)*(-1))
        else:
            print(heapq.heappop(p_heap))
    elif m_heap and not p_heap:
        print(heapq.heappop(m_heap)*(-1))
    elif not m_heap and p_heap:
        print(heapq.heappop(p_heap))
    else:
        print(0)
