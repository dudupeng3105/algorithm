from collections import defaultdict


def dfs(start):
    print(start, end=' ')
    visited.append(start)
    for i in connected_dict[start]:
        if not i in visited:
            dfs(i)

def bfs(start):
    discovered = [start]
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in connected_dict[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)    
    return print(*discovered)


N, M, V = map(int, input().split())  # vertax, edge, start
connected_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    # DFS 용 dict
    connected_dict[a].append(b)
    connected_dict[b].append(a)
    connected_dict[a].sort()
    connected_dict[b].sort()

# dfs 돌리기
# 시작이 V, DFS
visited = []
dfs(V)
print()
# BFS
bfs(V)
