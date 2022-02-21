from collections import defaultdict
import sys


sys.stdin = open("test.txt")


def dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered


vertax, edges = map(int, input().split())
edges_list = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(len(edges_list)//2):
    a, b = edges_list[2*i], edges_list[2*i + 1]
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1))
