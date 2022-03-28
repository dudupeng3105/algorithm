from collections import defaultdict


def dfs(s, e):
    visited[s] = True
    if s == e:
        return 1  # 거리

    for next_node in graph[s]:
        if not visited[next_node]:
            temp = dfs(next_node, e)
            if temp:
                temp += dist_map[s][next_node]
                return temp

    return 0


# input 받기
n, m = map(int, input().split())
graph = defaultdict(list)
dist_map = [[0 for _ in range(n+1)] for __ in range(n+1)]
for _ in range(n-1):
    a, b, dist = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    dist_map[a][b] = dist
    dist_map[b][a] = dist

for _ in range(m):
    start, end = map(int, input().split())
    visited = [False for _ in range(n + 1)]
    print(dfs(start, end) - 1)


