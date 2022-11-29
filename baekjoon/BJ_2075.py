import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap_5 = [-1000 for _ in range(n)]
heapq.heapify(heap_5)

for i in range(n):
    temp = list(map(int, input().split()))
    for num in temp:
        if num > heap_5[0]:
            heapq.heappop(heap_5)
            heapq.heappush(heap_5, num)

print(heap_5[0])