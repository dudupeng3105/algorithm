import sys
from collections import defaultdict


v, e = map(int, input().split())
arr = defaultdict(list)
for _ in range(e):  # a 출발, b 도착
    a, b = map(int, sys.stdin.readline().split())
    arr[b].append(a)  # 거꾸로 연결

wanted_work = int(input())
stack = [wanted_work]  # 거꾸로 찾아감
visited = [False for _ in range(v + 1)]
visited[wanted_work] = True
result = 0
# dfs
while stack:
    work = stack.pop()

    for next_work in arr[work]:
        if not visited[next_work]:
            visited[next_work] = True
            result += 1
            stack.append(next_work)

print(result)