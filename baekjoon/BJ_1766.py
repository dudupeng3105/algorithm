import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
inner_arrows = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inner_arrows[b] += 1


# 순서 구하기
heap = []
for i in range(1, n + 1):
    if inner_arrows[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    problem = heapq.heappop(heap)
    result.append(problem)
    for next_problem in graph[problem]:
        inner_arrows[next_problem] -= 1
        if inner_arrows[next_problem] == 0:
            heapq.heappush(heap, next_problem)

print(*result)

