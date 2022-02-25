import sys
from collections import deque, defaultdict
sys.stdin = open("test.txt")

v, e = map(int,input().split())
graph = defaultdict(list)
edges_lst = list(map(int,input().split()))
for i in range(e):
    a, b = edges_lst[2*i], edges_lst[2*i + 1]
    graph[a].append(b)
    graph[b].append(a)


# bfs
q = deque()
q.append(1)
visited = [False for _ in range(v+1)]
visited[1] = True

while q:
    node = q.popleft()
    print(f'-{node}', end="")

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            q.append(next_node)



