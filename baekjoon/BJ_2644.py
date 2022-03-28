from collections import defaultdict


def dfs(node, depth):
    visited[node] = True
    if node == end:
        return depth

    for next_node in graph[node]:
        if not visited[next_node]:
            result = dfs(next_node, depth + 1)
            if result > 0:
                return result

    return -1


# input 받기
n = int(input())
visited = [False for _ in range(n + 1)]
start, end = map(int, input().split())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(start, 0))  # node, depth