import sys
import heapq


input = sys.stdin.readline
n, k = map(int, input().split())
jewel_lst = []
bag_lst = []

for _ in range(n):
    m, v = map(int, input().split())
    jewel_lst.append([m, v])

for __ in range(k):
    bag_lst.append(int(input()))

jewel_lst.sort()
bag_lst.sort()

total = 0
h = []
for bag_weight in bag_lst:
    while jewel_lst and bag_weight >= jewel_lst[0][0]:
        heapq.heappush(h, -jewel_lst[0][1])  # max-heap
        heapq.heappop(jewel_lst)
    if h:
        total += heapq.heappop(h)
    elif not jewel_lst:  # 힙에 남은거도 없고 보석도 더 이상없다.
        break

print(-total)