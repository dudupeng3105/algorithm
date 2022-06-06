import sys
from collections import deque
input = sys.stdin.readline


tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    taken_time = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    inner_arrow = [0 for _ in range(n+1)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        inner_arrow[b] += 1
    # print(graph)
    # print(inner_arrow)
    w = int(input())

    q = deque()
    for i in range(1, n + 1):
        if inner_arrow[i] == 0:  # 선행 작업이 현재 없으면
            q.append(i)
            taken_time[i] = time[i]

    while q:
        work = q.popleft()
        for next_work in graph[work]:
            inner_arrow[next_work] -= 1
            taken_time[next_work] = max(taken_time[work]+time[next_work], taken_time[next_work])
            if inner_arrow[next_work] == 0:
                q.append(next_work)

    print(taken_time[w])