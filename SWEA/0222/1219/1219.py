import sys
from collections import defaultdict

sys.stdin = open("test.txt")


def dfs(start, end):
    path = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in path:
            path.append(node)
            for w in graph[node]:
                if w == end:
                    return 1
                else:
                    stack.append(w)

    return 0


for _ in range(1, 10 + 1):
    tc, num_edges = map(int, input().split())
    graph = defaultdict(list)
    given_list = list(map(int, input().split()))
    for i in range(num_edges):
        v1, v2 = given_list[2*i], given_list[2*i+1]
        graph[v1].append(v2)

    print(f'#{tc} {dfs(0, 99)}')