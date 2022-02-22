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


test_case = int(input())
for tc in range(1, test_case + 1):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    s, g = map(int, input().split())   # 출발노드, 도착노드
    print(f'#{tc} {dfs(s, g)}')


